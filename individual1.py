#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == "__main__":
   # Определим универсальное множество
   u = set("abcdefghijklmnopqrstuvwxyz")
   
   a = {"a", "b", "h", "j", "l"}
   b = {"b", "c", "h", "l", "r", "v"}
   c = {"j", "k", "n", "t", "z"}
   d = {"b", "i", "k", "v", "w"}
   
   x = (a.intersection(b)).union(c)
   print(f"x = {x}")
   
   # Найдем дополнения множеств
   bn = u.difference(b)
   cn = u.difference(c)
   
   y = (a.difference(d)).union(cn.difference(bn))
   print(f"y = {y}")