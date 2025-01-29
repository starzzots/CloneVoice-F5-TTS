from pydub import AudioSegment

def combine_wav_files(output_file, file_prefix, start, end):
    # Initialize the combined audio with the first file
    combined = AudioSegment.from_wav(f"c:\\Users\\Kyle\\Music\\space_ai\\{file_prefix}{start}.wav")
    
    # Loop through the remaining files and combine them
    for i in range(start + 1, end + 1):
        file_name = f"c:\\Users\\Kyle\\Music\\space_ai\\{file_prefix}{i}.wav"
        print(f"Processing: {file_name}")
        audio = AudioSegment.from_wav(file_name)
        combined += audio

    # Export the combined audio to the specified output file
    combined.export(output_file, format="wav")
    print(f"Combined audio saved to: {output_file}")

# Example usage
combine_wav_files(
    output_file="combined_audio.wav",  # Output file name
    file_prefix="p",                  # Prefix for file names
    start=1,                          # Starting number
    end=12                            # Ending number
)