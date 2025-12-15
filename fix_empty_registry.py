#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

path = 'validators/ophthalmic_optical.py'

with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    # 检查是否是以 = 结尾的 registry 行
    if 'registry[' in line and line.rstrip().endswith('='):
        # 在行尾添加 _validate_hundred_scale_score
        new_line = line.rstrip() + ' _validate_hundred_scale_score\n'
        new_lines.append(new_line)
    else:
        new_lines.append(line)

with open(path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f"Fixed {sum(1 for i, line in enumerate(lines) if 'registry[' in line and line.rstrip().endswith('='))} empty registry assignments")
