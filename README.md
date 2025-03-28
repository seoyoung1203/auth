 - {% csrf_token %}
 >> 우리꺼에서 만든거야 도장꽝

 - login
 User -> ID, password ->  ID, password(장고에게 주고) -> session을 발급(create_새로운 데이터 발급)(쿠키에)

```shell
 <nav class="nav">
        {% if user.is_authenticated %} # 검증됐을때 -> logout 버튼 나타나도록
            <a href="" class="nav-link disabled">{{user}}</a> 
            <a href="{% url 'accounts:logout' %}" class="nav-link">logout</a>

        {% else %} # 검증되지 않았을때 -> logout 버튼 나타나지 않음
            <a href="{% url 'accounts:signup' %}" class="nav-link">signup</a>
            <a href="{% url 'accounts:login' %}" class="nav-link">login</a>
         {% endif %}
```
- 여러개 연결 >> 모델링 한 번 더 (articles도 만들었다)

.get('next') 무조건 코드는 실행할라고.
next 인자가 있으면 --
없을때 -- none

```shell
<form action="{% url 'articles:comment_create' %}" method="POST">
```
action을 비워두면 자기자신으로 돌아가지만 여기서는 

