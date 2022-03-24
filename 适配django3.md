# `xadmin修改记录，基于webDjango项目`

# 20220123

* 复制可用版本，后面碰到问题再改

主要出错在plugins

django3中变量导包位置变动

* 更新font-awesome

前端图标文件 xadmin/static/xadmin/vendor/font-awesome

原来是4.0.3，更新到4.7.0

* 3.x版本中django.uitls中移除了six，但是xadmin中大量这样使用，在xadmin.__init__.py顶部运行位置，增加

```
import six
import django
setattr(django.utils, 'six', six)
```

# 20220122

1

```
  File "D:\0web\xadmin-django3\xadmin\views\list.py", line 225, in get_list_queryset
    except models.FieldDoesNotExist:
AttributeError: module 'django.db.models' has no attribute 'FieldDoesNotExist'
```

```
from django.core.exceptions import FieldDoesNotExist
```

2

```
  File "D:\0web\xadmin-django3\xadmin\plugins\filters.py", line 9, in <module>
    from django.db.models.fields import FieldDoesNotExist
```

```
# from django.db.models.fields import FieldDoesNotExist
from django.core.exceptions import FieldDoesNotExist
```

3

```
File "D:\0web\xadmin-django3\xadmin\models.py", line 19, in <module>
    from xadmin.util import quote
  File "D:\0web\xadmin-django3\xadmin\util.py", line 7, in <module>
    from django.forms.forms import pretty_name
```

```
# from django.forms.forms import pretty_name
from django.forms.utils import pretty_name
```

4

```
  File "D:\0web\1_muke\xadmin_ueditor_django\django3\xadmin\sites.py", line 7, in <module>
    from django.utils import six
```

3.x版本中django.uitls中移除了six，但是xadmin中大量这样使用，在xadmin.__init__.py顶部运行位置，增加

```
import six
import django
setattr(django.utils, 'six', six)
```

5

```
 File "D:\0web\1_muke\xadmin_ueditor_django\django3\xadmin\models.py", line 11, in <module>
    from django.utils.encoding import python_2_unicode_compatible, smart_text
```

```
# from django.utils.encoding import python_2_unicode_compatible, smart_text
from django.utils.encoding import smart_text
from six import python_2_unicode_compatible

```

6

```
  File "D:\0web\1_muke\xadmin_ueditor_django\django3\xadmin\models.py", line 20, in <module>
    from xadmin.util import quote
  File "D:\0web\1_muke\xadmin_ueditor_django\django3\xadmin\util.py", line 25, in <module>
    from django.contrib.staticfiles.templatetags.staticfiles import static

```

```
    # from django.contrib.staticfiles.templatetags.staticfiles import static
    from django.templatetags.static import static
```

7

```
File "D:\0web\1_muke\xadmin_ueditor_django\django3\xadmin\plugins\filters.py", line 9, in <module>
    from django.db.models.fields import FieldDoesNotExist
ImportError: cannot import name 'FieldDoesNotExist' from 'django.db.models.fields' (D:\Anaconda3\envs\django3\lib\site-packages\django\db\models\fields\__init__.py)

```

```
# from django.db.models.fields import FieldDoesNotExist
from django.core.exceptions import FieldDoesNotExist
```
