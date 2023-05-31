# import하고 싶은 모듈이 있으면 import구문을 사용
# from module_test import module_statements
# from 패키지 명 import 파일명 또는 import 패키지명.파일명
# as를 사용하여 약어로도 사용가능
# import modul_test.modul_statements as ms
# print(modul_statements.plus(10,20))
# ex) 패키지이면(폴더)
# import module_folder.module_statements
# from module_folder import module_statements as ms
# as를 써서 별칭으로도 할 수 있다
import module_statements
print(module_statements.plus(10,20))
c1 = module_statements.Calculator()
c1.plus(10)
print(c1.result)