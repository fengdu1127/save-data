encoding='utf8'
import jieba
seg_list = jieba.cut("���������羰�ܺã�������ʤ�أ�",
                     cut_all=False)
print("Full Mode: " + "/ ".join(seg_list))  # ȫģʽ