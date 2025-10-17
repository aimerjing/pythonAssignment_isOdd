import sys
import importlib.util
import types

def load_module():
    """动态加载学生模块"""
    try:
        spec = importlib.util.spec_from_file_location("student_module", "main.py")
        student_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(student_module)
        return student_module
    except Exception as e:
        print(f"❌ 导入学生模块失败: {e}")
        return None

def run_tests():
    """运行测试用例"""
    module = load_module()
    if not module or not hasattr(module, 'isOdd'):
        print("❌ 未找到 isOdd 函数")
        return False
    
    isOdd = module.isOdd
    
    test_cases = [
        # 整数测试
        (1, True),         # 正奇数
        (3, True),         # 正奇数
        (-5, True),        # 负奇数
        (0, False),        # 零
        (2, False),        # 正偶数
        (-4, False),       # 负偶数
        
        # 非整数测试
        (3.0, False),      # 浮点整数
        (3.5, False),      # 浮点数
        ("5", False),      # 字符串数字
        ("hello", False),  # 字符串
        ([1, 3, 5], False),# 列表
        ({}, False),       # 字典
        (None, False),     # None
        (True, False),     # 布尔值
        (False, False),    # 布尔值
        (isOdd, False)     # 函数本身
    ]
    
    passed = 0
    total = len(test_cases)
    
    for input_val, expected in test_cases:
        try:
            result = isOdd(input_val)
            if result == expected:
                print(f"✅ 测试通过: {repr(input_val)} -> {expected}")
                passed += 1
            else:
                print(f"❌ 测试失败: {repr(input_val)}")
                print(f"   预期: {expected} | 实际: {result}")
        except Exception as e:
            print(f"❌ 异常错误: {repr(input_val)}")
            print(f"   异常: {e}")
    
    print(f"\n测试结果: {passed}/{total} 通过")
    if passed == total:
        print("🎉 所有测试通过!")
        return True
    else:
        print("💥 存在未通过的测试")
        return False

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
