from cryptosteganography import CryptoSteganography


# open sound file
mediafile = 'song.mp3'
message = None
with open(mediafile, "rb") as f:
  # I just embeded a small portion of the song, not all of it
  message = f.read(120000)

print()
print('The program is looking for an image named nebula.png\n')
origfile = "nebula.png"
print('The image with the hidden audio file will be called steg_audio_nebula.png\n')
modfile = "steg_audio_nebula.png"
key = "1111222233334444!"
crypto_steganography = CryptoSteganography(key)
crypto_steganography.hide(origfile, modfile, message)
print('The extracted data will be called decrypted_song.mp3 \n')
decrypted = 'decrypted_song.mp3'
secret_bin = crypto_steganography.retrieve(modfile)
# Save the data to a new file
with open(decrypted, 'wb') as f:
  f.write(secret_bin)