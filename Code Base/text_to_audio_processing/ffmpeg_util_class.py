import os
import subprocess
import time
from natsort import natsorted


class Ffmpeg_Util:
    base_dir = "/Path/To/audio_files2/"
    audio_files = base_dir + "audio_list.txt"
    output_file = base_dir + "output.wav"

    def compile_files(self, base_dir, output_file):

        self.base_dir = base_dir
        self.output_file = output_file

        # where to seek the files
        file_list = open(self.audio_files, "w")

        # remove prior output
        try:
            os.remove(output_file)
        except OSError:
            pass

        # scan for the video files
        start = time.time()
        for root, dirs, files in os.walk(base_dir):
            for video in files:
                if video.endswith(".wav") and ("wout" in video):
                    file_list.write("file './%s'\n" % video)
        file_list.close()

        # Read lines from the input file
        with open(self.audio_files, 'r') as infile:
            lines = infile.readlines()
        # Sort lines based on the second column (assuming it contains numerical values)
        sorted_lines = natsorted(lines, key=lambda line: line.lower())
        # Write sorted lines to a new output file
        with open(self.audio_files, 'w') as outfile:
            outfile.writelines(sorted_lines)

        # merge the video files
        cmd = ["ffmpeg",
               "-f",
               "concat",
               "-safe",
               "0",
               "-loglevel",
               "quiet",
               "-i",
               "%s" % self.audio_files,
               "-c",
               "copy",
               "%s" % self.output_file
               ]

        #filters = 'silenceremove=1:0:-50dB:0:1:-50dB:d=0.5'
        p = subprocess.Popen(cmd, stdin=subprocess.PIPE)

        fout = p.stdin
        fout.close()
        p.wait()

        print(p.returncode)
        if p.returncode != 0:
            raise subprocess.CalledProcessError(p.returncode, cmd)

        end = time.time()
        print("Merging the files took", end - start, "seconds.")


def remove_silence(input_file, output_file):
    # Define the FFmpeg command to remove silence
    command = [
        'ffmpeg',
        '-i', input_file,
        '-af', 'silenceremove=start_periods=1:start_duration=1:start_threshold=-50dB:stop_periods=1:stop_duration=1:stop_threshold=-50dB',
        output_file
    ]


if __name__ == "__main__":
    ffmpeg_util = Ffmpeg_Util()
    print ("VALUES==========" + str (ffmpeg_util.base_dir) + "        val2=" + str(ffmpeg_util.output_file))
    ffmpeg_util.compile_files(ffmpeg_util.base_dir, ffmpeg_util.output_file)