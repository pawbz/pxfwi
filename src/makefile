

file_names = $(shell find . -name "*.py")
remove_tabs = $(file_names:./%.py=%.rtabs)


default:
	chmod a+x pxfwi.py
	ln -fs pxfwi.py pxfwi
	 
# convert tabs to spaces in all source files
rtabs: $(remove_tabs)
%.rtabs: %.py
	cp $< $*.d
	expand $*.d >$< 
	rm *.d

