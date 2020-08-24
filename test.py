<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>个人中心</title>
</head>
<body>
{% if img_url %}
    <img src="{{ img_url }}" alt="">
{% endif %}
<form action="" enctype="multipart/form-data" method="post">
    <input type="file" name="photo" />
    <input type="submit" value="立即提交">
</form>
</body>
</html>