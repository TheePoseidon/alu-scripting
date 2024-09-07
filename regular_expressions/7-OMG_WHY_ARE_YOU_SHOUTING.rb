#!/usr/bin/env ruby

if ARGV.length != 1
  puts "Usage: ./7-OMG_WHY_ARE_YOU_SHOUTING.rb <string>"
  exit 1
end

input = ARGV[0]
puts input.scan(/[A-Z]+/).join
