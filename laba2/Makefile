all: run

.PHONY: all run clean

build/:
	mkdir $@

build/main: main.cc | build/
	clang++ -Wall -Wextra -Wpedantic -Werror -Wno-unused -std=c++23 -O3 -o $@ $<

run: build/main
	@$<

clean:
	rm -rf build/
