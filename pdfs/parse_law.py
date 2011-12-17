#!/usr/bin/python
# -*- coding:Utf-8 -*-
import os
import re

def pdf_to_text(pdf_name):
    os.system("pdftotext -layout %s" % pdf_name)
    return open(pdf_name.replace(".pdf", ".txt"), "r").read()

def remove_useless_informations(text):
    result = []
    for i in text.split("\n")[1:]:
        if "DOC 53" in i:
            continue
        if re.match("^CHAMBRE .* ZITTINGSPERIODE$", i):
            continue
        if re.match("^ *\d\d\d\d *$", i):
            continue
        if "Imprimerie centrale – Cette publication est imprimée exclusivement sur du papier certiﬁé FSC" in i:
            continue
        if "Centrale drukkerij – Deze publicatie wordt uitsluitend gedrukt op FSC gecertiﬁceerd papier" in i:
            continue
        else:
            result.append(i)
    return "\n".join(result)

def parse(pdf_name):
    text = pdf_to_text(pdf_name)
    text = remove_useless_informations(text)
    print text

if __name__ == "__main__":
    parse("53K1961001.pdf")
