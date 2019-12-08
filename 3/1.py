def run(lines):
    pass


#Ill fated attempt using vectors and line segment math
# def run(lines):
#     v1 = parse(lines[0].split(','))
#     v2 = parse(lines[1].split(','))
#
#     s1 = normalize_segments(segments(v1))
#     s2 = normalize_segments(segments(v2))
#
#     i = intersections(s1, s2)
#     print(f"i: {i}")
#
# def normalize_segments(segments):
#     out = []
#
#     for (start, end) in segments:
#         if(start[0] > end[0] or start[1] > end[1]):
#             start, end = end, start
#
#         out.append( (start, end) )
#
#     return out
#
# def intersections(first_segments, second_segments):
#     out = []
#
#     for s1 in first_segments:
#         for s2 in second_segments:
#             point = intersect(s1, s2)
#
#             if(point):
#                 out.append(point)
#
#     return out
#
# def intersect(s1, s2):
#     #S2 has either its start or end point between s1 (x axis)
#     x = s1[0][0] <= s2[0][0] <= s1[1][0] or s1[0][0] <= s2[1][0] <= s1[1][0]
#     #S2 has either its start or end point between s1 (y axis)
#     y = s1[0][1] <= s2[0][1] <= s1[1][1] or s1[0][1] <= s2[1][1] <= s1[1][1]
#
#     if(x and y):
#         out = [None, None]
#         #Vertical
#         if(s1[0][0] == s1[1][0]):
#             out[0] = s1[0][0]
#         else:
#             out[1] = s1[0][1]
#
#         if(s2[0][0] == s2[1][0]):
#             out[0] = s2[0][0]
#         else:
#             out[1] = s2[0][1]
#
#         return out
#
#     return False
#
#
#
#
#
#
# def parse(dirs):
#     out = []
#
#     for dir in dirs:
#         if dir[0] == 'R':
#             out.append( (int(dir[1:]),0) )
#         elif dir[0] == 'D':
#             out.append( (0, -int(dir[1:])) )
#         elif dir[0] == 'L':
#             out.append( (-int(dir[1:]),0) )
#         else:
#             out.append( (0, int(dir[1:])) )
#
#     return out
#
# def segments(vectors):
#     s = (0, 0)
#     segments = []
#
#     for v in vectors:
#         e = (s[0] + v[0], s[1] + v[1])
#         segments.append( (s, e) )
#         s = e
#
#     return segments
