def score(Img1, Img2):
    identical = 0
    for tag in Img1["tags"]:
        for tag2 in Img2["tags"]:
            if tag == tag2:
                identical += 1
    return min(identical, Img1["nb_tags"] - identical, Img2["nb_tags"] - identical)


def total_score(photos):
    t_score = 0
    for i in range(len(photos) - 1):
        t_score += score(photos[i], photos[i+1])
    return t_score
