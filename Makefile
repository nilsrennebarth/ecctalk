all: images

# Elliptic curves examples
ECEXAMPLES := \
	ec1-m2-p2.png \
	ec2-m2-p1.png \
	ec3-p1-p0.png \
	ec4-p0-p4.png \
	nec-m3-p2.png

$(ECEXAMPLES): ecurve.py

ec1-m2-p2.png:
	python3 ecurve.py a=-2 b=2 xrange=-2,4 yrange=-4,4 $@

ec2-m2-p1.png:
	python3 ecurve.py a=-2 b=1 xrange=-2,4 yrange=-4,4 $@

ec3-p1-p0.png:
	python3 ecurve.py a=1 b=0 xrange=-1,4 yrange=-4,4 $@

ec4-p0-p4.png:
	python3 ecurve.py a=0 b=4 xrange=-3,4 yrange=-4,4 $@

nec-m3-p2.png:
	python3 ecurve.py a=-3 b=2 xrange=-4,4 yrange=-4,4 $@

images: $(ECEXAMPLES)



clean:
	rm -f $(ECEXAMPLES)

.PHONY: all images clean
