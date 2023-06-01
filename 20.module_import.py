# import하고 싶은 모듈(.py를 의미)이 있으면 import구문을 사용
# 디렉터리는 모듈을 포함하고 있는 패키지
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

import classstatements # 숫자.이 나오면 안되는거같은디 이유좀..지금 이름은 
c1 = classstatements.CalculatorChild()

c1.plus(100)
print(f"module_import의 result : ", {c1.result})

