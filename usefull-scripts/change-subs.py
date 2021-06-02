
with open ("I:\TORRENT\HighS\High School Musical (2006) [BluRay] [1080p] [YTS.AM]\subs.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    # print(lines)

for line in lines:
    line.replace('œ', 's')
    line.replace('œ','ś')
    line.replace('¹', 'ą')
    print(line)

#Warto pamiętać o sposobie zapisu ENCODING :)