from imagesoup import ImageSoup
import time
soup = ImageSoup()

start_time = time.time()

images = soup.search('"Narendra Modi"', n_images=1000)

# search query returned only 807 results :()
for i in range(len(images)):
	k = images[i]
	url_link = k.URL
	print url_link
	extention = url_link.split(".")
	extentionstr = str(extention[-1])
	extentionstr = extentionstr.strip('/\\')
	extentionstr = extentionstr.strip('?\\')

	file_name = str(i)+"-namo."+extentionstr
	try:
		k.to_file(file_name)
		print "saved file ", i
	except:
		print "some error occured"

	if(i%15 == 0):
		print "sleeping :( "
		time.sleep(5)
		print "woke up ^-^"

print("--- %s seconds ---" % (time.time() - start_time))

# saved file  806
# --- 1624.08369803 seconds ---
