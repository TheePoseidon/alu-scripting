#!/usr/bin/env ruby

# Ensure we have an input argument
if ARGV.length != 1
  puts "Usage: ./8-textme.rb '<log_message>'"
  exit 1
end

log_message = ARGV[0]

# Use regex to extract sender, receiver, and flags
sender_match = log_message.match(/\[from:(.+?)\]/)
receiver_match = log_message.match(/\[to:(.+?)\]/)
flags_match = log_message.match(/\[flags:(.+?)\]/)

if sender_match && receiver_match && flags_match
  sender = sender_match[1]
  receiver = receiver_match[1]
  flags = flags_match[1]

  # Output in the required format
  puts "#{sender},#{receiver},#{flags}"
else
  puts "Error: Could not extract necessary fields."
end
