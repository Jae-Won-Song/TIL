import requests

res = requests.get('https://api.themoviedb.org/3/movie/popular?api_key=5a6c767eeec67807ca0c5e4b2db72f24&language=en-US&page=1')

data = res.json()

# print(data)
#  불러온 데이터results에서 
#  title값을 개수로 뽑아낸다
# Problem A
def popular_count():
    title_num =[]    
    for movie_dic in (data['results']):
        t = movie_dic["title"]
        title_num.append(t)
    return len(title_num)
# print(popular_count())



# Problem B

# 인기영화정보에서 평점을 기준으로 점수8 영화들의 목록 리스트


a = []
for movie_star in (data['results']):
    #print(movie_star['vote_average'])
   # print(movie_star['title'])
    a.append([movie_star['vote_average'], movie_star['title']])

for moviestar in a:
    if moviestar[0] >= 8.0:
        print(moviestar)
