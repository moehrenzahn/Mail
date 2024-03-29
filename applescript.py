#!/usr/bin/python

import subprocess

def asrun(ascript):
  # "Run the given AppleScript and return the standard output and error."

  osa = subprocess.Popen(['osascript', '-'],
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE)
  return osa.communicate(ascript.encode())[0]

def asquote(astr):
  # "Return the AppleScript equivalent of the given string."
  
  astr = astr.replace('"', '" & quote & "')
  return '"{}"'.format(astr)
