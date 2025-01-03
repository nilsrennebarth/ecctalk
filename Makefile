all: images ellpress.pdf

# Elliptic curves examples
ECEXAMPLES := \
	ec1-m2-p2.png \
	ec2-m2-p1.png \
	ec3-p1-p0.png \
	ec4-p0-p4.png \
	nec-m3-p2.png

$(ECEXAMPLES): ecurve.py

EPOINTS = ec5-m1-p1-add.png ec6-m1-p1-points.png ec7-addpt-000.png finplot.png

ALLIMG := $(ECEXAMPLES) $(EPOINTS)

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

ec5-m1-p1-add.png: ecadd.py ecurve.py
	python3 ecadd.py

ec6-m1-p1-points.png: epoints.py ecurve.py
	python3 epoints.py
ec7-addpt-000.png: epointmulti.py ecurve.py
	python3 epointmulti.py
finplot.png: fincurve.py
	python3 fincurve.py

ellpress.pdf: ellpress.tex $(ALLIMG)
	lualatex ellpress

ELLPRESSGEN := \
	ellpress.aux \
	ellpress.log \
	ellpress.nav \
	ellpress.out \
	ellpress.pdf \
	ellpress.snm \
	ellpress.toc


images: $(ALLIMG)

clean:
	rm -f $(ALLIMG) ec7-addpt-0??.png $(ELLPRESSGEN)

.PHONY: all images clean
