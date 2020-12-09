# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 12:19:49 2020

@author: Admin
"""


import gtk
class PyApp(gtk.Window):
   def __init__(self):
      super(PyApp, self).__init__()
      self.set_default_size(300,200)
      self.set_title("Hello World in PyGTK")
      label = gtk.Label("Hello World")
      self.add(label)
      self.show_all()
PyApp()
gtk.main()