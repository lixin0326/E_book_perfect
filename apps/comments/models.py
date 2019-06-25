from django.db import models


# 　分类书籍
class Book_classify2(models.Model):
    cla_id = models.AutoField(primary_key=True, verbose_name="分类id")
    name = models.CharField(max_length=20, verbose_name="书籍类别")

    class Meta:
        db_table = "book_classify2"
        verbose_name = "书籍类别"
        verbose_name_plural = verbose_name


# 　书的信息
class Book2(models.Model):
    book_id = models.IntegerField(default=0, verbose_name="书的id")
    image_url = models.CharField(max_length=100, verbose_name="图书封面地址")
    book_name = models.CharField(max_length=20, verbose_name="书名")
    author = models.CharField(max_length=50, verbose_name="作者")
    info = models.CharField(max_length=200, verbose_name="简介")
    price = models.IntegerField(default=0, verbose_name="图书价格")
    is_delete = models.IntegerField(default=0, verbose_name="图书是否下架")
    classify = models.ForeignKey(Book_classify2,
                                 models.DO_NOTHING,
                                 db_column='cla_id',
                                 db_index=True,
                                 verbose_name="书籍分类")

    def __str__(self):
        return self.book_name

    class Meta:
        db_table = "book2"
        verbose_name = "书名"
        verbose_name_plural = verbose_name


# 章节信息
class Book_Chapter(models.Model):
    chapter_id = models.AutoField(primary_key=True, verbose_name="章节ID")
    c_name = models.CharField(max_length=300, verbose_name="章节名称")
    c_url = models.CharField(max_length=200, verbose_name="章节地址")
    book_id = models.IntegerField(default=0, verbose_name="章节")

    def __str__(self):
        return self.c_name

    class Meta:
        db_table = "book_chapter"
        verbose_name = "章节信息"
        verbose_name_plural = verbose_name
