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