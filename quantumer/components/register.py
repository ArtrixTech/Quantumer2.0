#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Artrix"


def load_register(core):
    core.register_judge_function = register_judge_function
    core.register_extract_function = register_extract_function
    core.register_trigger_function = register_trigger_function


def register_trigger_function(self):

    def dec(func):
        self.trigger_function = func
        if all([self.trigger_function, self.extract_function]):
            self.function_inited = True
        return func
    return dec


def register_judge_function(self):

    def dec(func):
        self.judge_function = func
        return func
    return dec


def register_extract_function(self):

    def dec(func):
        self.extract_function = func
        if all([self.trigger_function, self.extract_function]):
            self.function_inited = True
        return func
    return dec
