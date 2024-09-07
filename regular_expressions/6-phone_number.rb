#!/usr/bin/env ruby

if ARGV.length != 1
  puts "Usage: ./6-phone_number.rb <phone_number>"
  exit 1
end

input = ARGV[0]

if input.match(/^\d{3}[- ]?\d{3}[- ]?\d{4}$/)
  puts input
end
