add_test([=[BasicAdapters.FilterOnly]=]  D:/Desktop/labwork9/out/build/x64-Debug/tests/adapter_tests.exe [==[--gtest_filter=BasicAdapters.FilterOnly]==] --gtest_also_run_disabled_tests)
set_tests_properties([=[BasicAdapters.FilterOnly]=]  PROPERTIES WORKING_DIRECTORY D:/Desktop/labwork9/out/build/x64-Debug/tests SKIP_REGULAR_EXPRESSION [==[\[  SKIPPED \]]==])
add_test([=[BasicAdapters.TransformOnly]=]  D:/Desktop/labwork9/out/build/x64-Debug/tests/adapter_tests.exe [==[--gtest_filter=BasicAdapters.TransformOnly]==] --gtest_also_run_disabled_tests)
set_tests_properties([=[BasicAdapters.TransformOnly]=]  PROPERTIES WORKING_DIRECTORY D:/Desktop/labwork9/out/build/x64-Debug/tests SKIP_REGULAR_EXPRESSION [==[\[  SKIPPED \]]==])
add_test([=[BasicAdapters.DropOnly]=]  D:/Desktop/labwork9/out/build/x64-Debug/tests/adapter_tests.exe [==[--gtest_filter=BasicAdapters.DropOnly]==] --gtest_also_run_disabled_tests)
set_tests_properties([=[BasicAdapters.DropOnly]=]  PROPERTIES WORKING_DIRECTORY D:/Desktop/labwork9/out/build/x64-Debug/tests SKIP_REGULAR_EXPRESSION [==[\[  SKIPPED \]]==])
add_test([=[BasicAdapters.ReverseOnly]=]  D:/Desktop/labwork9/out/build/x64-Debug/tests/adapter_tests.exe [==[--gtest_filter=BasicAdapters.ReverseOnly]==] --gtest_also_run_disabled_tests)
set_tests_properties([=[BasicAdapters.ReverseOnly]=]  PROPERTIES WORKING_DIRECTORY D:/Desktop/labwork9/out/build/x64-Debug/tests SKIP_REGULAR_EXPRESSION [==[\[  SKIPPED \]]==])
add_test([=[EdgeCases.DropAllElements]=]  D:/Desktop/labwork9/out/build/x64-Debug/tests/adapter_tests.exe [==[--gtest_filter=EdgeCases.DropAllElements]==] --gtest_also_run_disabled_tests)
set_tests_properties([=[EdgeCases.DropAllElements]=]  PROPERTIES WORKING_DIRECTORY D:/Desktop/labwork9/out/build/x64-Debug/tests SKIP_REGULAR_EXPRESSION [==[\[  SKIPPED \]]==])
add_test([=[ContainerTypes.DequeWithTransform]=]  D:/Desktop/labwork9/out/build/x64-Debug/tests/adapter_tests.exe [==[--gtest_filter=ContainerTypes.DequeWithTransform]==] --gtest_also_run_disabled_tests)
set_tests_properties([=[ContainerTypes.DequeWithTransform]=]  PROPERTIES WORKING_DIRECTORY D:/Desktop/labwork9/out/build/x64-Debug/tests SKIP_REGULAR_EXPRESSION [==[\[  SKIPPED \]]==])
add_test([=[Combinations.FilterTransform]=]  D:/Desktop/labwork9/out/build/x64-Debug/tests/adapter_tests.exe [==[--gtest_filter=Combinations.FilterTransform]==] --gtest_also_run_disabled_tests)
set_tests_properties([=[Combinations.FilterTransform]=]  PROPERTIES WORKING_DIRECTORY D:/Desktop/labwork9/out/build/x64-Debug/tests SKIP_REGULAR_EXPRESSION [==[\[  SKIPPED \]]==])
add_test([=[Combinations.DropTransform]=]  D:/Desktop/labwork9/out/build/x64-Debug/tests/adapter_tests.exe [==[--gtest_filter=Combinations.DropTransform]==] --gtest_also_run_disabled_tests)
set_tests_properties([=[Combinations.DropTransform]=]  PROPERTIES WORKING_DIRECTORY D:/Desktop/labwork9/out/build/x64-Debug/tests SKIP_REGULAR_EXPRESSION [==[\[  SKIPPED \]]==])
add_test([=[StringTests.TransformStrings]=]  D:/Desktop/labwork9/out/build/x64-Debug/tests/adapter_tests.exe [==[--gtest_filter=StringTests.TransformStrings]==] --gtest_also_run_disabled_tests)
set_tests_properties([=[StringTests.TransformStrings]=]  PROPERTIES WORKING_DIRECTORY D:/Desktop/labwork9/out/build/x64-Debug/tests SKIP_REGULAR_EXPRESSION [==[\[  SKIPPED \]]==])
set(  adapter_tests_TESTS BasicAdapters.FilterOnly BasicAdapters.TransformOnly BasicAdapters.DropOnly BasicAdapters.ReverseOnly EdgeCases.DropAllElements ContainerTypes.DequeWithTransform Combinations.FilterTransform Combinations.DropTransform StringTests.TransformStrings)
