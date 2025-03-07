all: run

.PHONY: all run clean

build/:
	mkdir $@

build/main: main.cc | build/
	clang++ -std=c++20 -o $@ $<

run: build/main
	$<

clean:
	rm -rf build/
