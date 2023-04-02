#! By HookSander

import os
from pytube import Playlist

def userLink():
    print("===================================")
    print("= Youtube Playlist MP3 Downloader =")
    print("=        github.com/ha-bib        =")
    var = input("===================================\nMasukkan tautan playlist YouTube Anda \n=> ")
    downloadFile = Playlist(var)
    return downloadFile


def userPath():
    var = input("\nMasukkan path folder tujuan\n=> ")
    return var


def valide():
    user = input("Apakah Anda ingin mengunduh playlist ini? [Y/o]\n=> ").lower()
    if user == 'y':
        return True
    else:
        return False


def download(playlist, uPath):
    print("\nMemproses...") 
    if not os.path.exists(uPath):
        print("Membuat Folder")
        os.makedirs(uPath)
    playlistLen = len(playlist.videos) 
    print("\nMengunduh playlist: {}\nJumlah video: {}\n\n".format(playlist.title, playlistLen))
    count = 0
    if valide():
        for video in playlist.videos:
            count += 1 
            print("\nMengunduh lagu {}/{} - {}".format(count, playlistLen, video.title))
            audioFile = video.streams.filter(only_audio=True).order_by('abr').desc().first()
            if audioFile.abr >= "128kbps":
                file = audioFile.download(output_path=uPath)
                base, ext = os.path.splitext(file)
                newFile = base + ".mp3"
                os.rename(file, newFile)
                print("Selesai diunduh. Kualitas audio: {}".format(audioFile.abr))
            else:
                print("Tidak dapat menemukan kualitas audio yang tepat untuk {}. Lagu ini dilewati.".format(video.title))
        print("\nUnduhan selesai.")
    else:
        input("Tekan Enter untuk keluar, pengunduhan dibatalkan.")


if __name__ == '__main__':
    download(userLink(), userPath())
    input("Tekan Enter untuk keluar...")  
