from youtube_transcript_api import YouTubeTranscriptApi as youTube
import scrapetube as allChanellsVideo


def getAllVideosIdFromChannel(chanelUrl: str):
    allIds = []
    videos = allChanellsVideo.get_channel(channel_url=chanelUrl)
    for i in videos:
        allIds.append(i["videoId"])
    return allIds

def getAllVideosTranscription(videosId: str):
    allTranscriptions = []
    allVideosId = []
    for video in videosId:
        allVideosId.append(video)
        allTranscriptions.append(getAllTextInLowerCase(video))

    return allTranscriptions



def getAllTextInLowerCase(videoId: int):
    finalText = "  "
    try:
        textLibrary = youTube.get_transcript(videoId, languages=["ru", "en"])
        for i in textLibrary:
            finalText += i["text"]
        finalText = finalText.replace(" ", "")
        finalText = finalText.replace( "-", "")
        finalText = finalText.replace(".", "")
        finalText = finalText.lower()
    except Exception:
        finalText = "no_transcript"
    return finalText

def findVideo(text: str, videoTranscriptions,  videosIds):
    text = text.lower()
    text = text.replace(" ", "")
    resIds = []
    for i in range(0, len(videoTranscriptions)):
        if text in videoTranscriptions[i]:
            resIds.append(videosIds[i])
    return resIds


searchedText = input("Insert the text you want to find -> ")
searchedText = searchedText.lower()
searchedText = searchedText.replace(" ", "")
res = findVideo(searchedText, getAllVideosTranscription(getAllVideosIdFromChannel("https://www.youtube.com/@tiam509")),
                          getAllVideosIdFromChannel("https://www.youtube.com/@tiam509"))

if len(res) != 0:
    print("Here are the videos with searched text: ")
    for i in res:
        print("https://www.youtube.com/watch?v=" + i)
else:
    print("It was not found")

#getAllVideosTranscription(getAllVideosIdFromChannel("https://www.youtube.com/@tiam509"))



