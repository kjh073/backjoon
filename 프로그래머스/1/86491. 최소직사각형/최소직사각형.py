def solution(sizes):
    max_h, max_w = 0, 0
    for size in sizes:
        if size[0] > size[1]:
            size[0], size[1] = size[1], size[0]
            
    for size in sizes:
        if size[0] > max_h:
            max_h = size[0] 
        if size[1] > max_w:
            max_w = size[1] 
            
    return max_h * max_w