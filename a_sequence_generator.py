#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""generate a integer sequence for testing"""

import numpy as np


def generate_sequence(count=30):
    return [np.random.randint(0, 100) for i in range(count)]