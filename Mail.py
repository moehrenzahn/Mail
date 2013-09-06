import os
import sys
import sublime
import sublime_plugin
from Mail.applescript import asrun, asquote # Thanks to Dr. Drang (http://www.leancrew.com/all-this/2013/03/combining-python-and-applescript/)

class MailCommand(sublime_plugin.WindowCommand):

    def run(self):
        view = self.window.active_view()

        if view:
            body = self.getBody()
            subject = self.getSubject()
            
            ascript = '''

            tell application "Mail"
                set theMessage to make new outgoing message with properties {{visible:true, subject:{0}, content:{1}}}
                activate
            end tell

            '''.format(asquote(subject), asquote(body))
            asrun(ascript)
    
    def getBody(self):
        view = self.window.active_view()
        afterFirstLine = sublime.Region.size(view.full_line(1))
        return view.substr(sublime.Region(afterFirstLine, view.size()))

    def getSubject(self):
        view = self.window.active_view()
        return view.substr(view.line(1))