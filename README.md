# PytestTutorial

## Installation
```bash
python -m pip install pytest==2.9.1
```
**2.9.1** is the pytest **version** will be installed

### Reading Pytest Output

&nbsp; &nbsp; &nbsp; &nbsp; **F** say failure

&nbsp; &nbsp; &nbsp; &nbsp; **Dot(.)** says success

>**How pytest identifies the test files and test methods**  
>&nbsp; _By default pytest only identifies the file names starting with test_ or ending with _test as the test files. We can explicitly mention other filenames though (explained later)_  
>&nbsp; _Pytest requires the test method names to start with "test." All other method names will be ignored even if we explicitly ask to run those methods_

## Running Tests
### From a specific file and multiple files.
Inside folder tests/ we have test_assert.py. To run all tests inside that folder, from root directory
```bash
cd tests
py.test 
```

To run test from a specific file
```bash
py.test test_assert.py
```
### Run a subset of test suite
Sometimes we don't want to run the entire test suite. Pytest allows us to run specific tests. We can do it in 2 ways  
* Grouping of test names by substring matching  
* Grouping of tests by markers  
Currently, we have  
test_assert.py    
&nbsp; &nbsp; &nbsp; &nbsp; test_method0  
&nbsp; &nbsp; &nbsp; &nbsp; test_method1

**Option 1) Run tests by substring matching**  
Here to run all tests having **methods** in its name we have to run
```bash  
py.test -k method -v
-k <expression> is used to represent the substring to match
-v increases the verbosity
```
**Option 2) Run tests by markers**  
Pytest allows us to set various attributes for the test methods using pytest markers, @pytest.mark
Here we will apply different marker names to test methods and run specific tests based on marker names. We can define the markers on each test names by using
```bash  
@pytest.mark.<name>
```
_Example:_
```python  
import pytest
1
@pytest.mark.group2
def test_method0():
	x, y = 5, 6
	assert x+1 == y, "Test Addition, assertion failed"
	assert x == y , "Assertion failed"

@pytest.mark.group1
def test_method1():
	x, y = 5, 6
	assert x+1 ==y, "Test test_method1 failed"

@pytest.mark.group2
def test_methods2():
	x, y = 5, 6
	assert x+1 == y, "Test Addition, assertion failed"
	assert x == y , "Assertion failed"

@pytest.mark.group1
def test_methods3():
	x, y = 5, 6
	assert x+1 ==y, "Test test_method1 failed"
```
We can run the marked test by
```bash  
py.test -m <name>
-m <name> mentions the marker name
```
Run `py.test -m group1` will run the methods **test_method1()** and **test_method3()**  
&nbsp; **Register markers for your test suite**  
```bash
# pytest.ini
[pytest]
minversion = 6.1.0
addopts = -ra -q
testpaths = 
	tests
markers = 
	group1: Mark as a group 01
	group2: Mark as a group 02

```

## Running Tests in parallel
Usually, a test suite will have multiple test files and hundreds of test methods which will take a considerable amount of time to execute. Pytest allows us to run tests in parallel.  
For that we need to first install pytest-xdist by running
```bash  
pip install pytest-xdist
```  
You can run tests now by
```bash  
py.test -n 4  
-n <num> runs the tests by using multiple workers. In the above command, there will be 4 workers to run the test
```

## Pytest Fixtures
### Basic Fixtures
Fixtures are used when we want to run some code before every test method. So instead of repeating the same code in every test we define fixtures. Usually, fixtures are used to initialize database connections, pass the base , etc
A method is marked as a fixture by marking with `@pytest.fixture`    
A test method can use a fixture by mentioning the fixture as an input parameter.
```python
import pytest
@pytest.fixture
def supply_AA_BB_CC():
	aa=25
	bb =35
	cc=45
	return [aa,bb,cc]

def test_comparewithAA(supply_AA_BB_CC):
	zz=35
	assert supply_AA_BB_CC[0]==zz,"aa and zz comparison failed"

def test_comparewithBB(supply_AA_BB_CC):
	zz=35
	assert supply_AA_BB_CC[1]==zz,"bb and zz comparison failed"

def test_comparewithCC(supply_AA_BB_CC):
	zz=35
	assert supply_AA_BB_CC[2]==zz,"cc and zz comparison failed"
```
Here we have
* A fixture named supply_AA_BB_CC. This method will return a list of 3 values.  
* 3 test methods comparing against each of the values.  
Each of the test function has an input argument whose name is matching with an available fixture. Pytest then invokes the corresponding fixture method and the returned values will be stored in the input argument , here the list [25,35,45]. Now the list items are being used in test methods for the comparison.  
> _The fixture method has a _**scope only within that test file**_ it is defined. If we try to access the fixture in some other test file , we will get an error saying fixture 'supply_AA_BB_CC' not found for the test methods in other files._

### Using Fixtures against multiple test files 
## Parameterized tests
The purpose of parameterizing a test is to run a test against multiple sets of arguments. We can do this by `@pytest.mark.parametrize`
We will see this with the below example. Here we will pass 3 arguments to a test method. This test method will add the first 2 arguments and compare it with the 3rd argument.  
Create the test file test_addition.py with the below code
```python
import pytest
@pytest.mark.parametrize("input1, input2, output",[(5,5,10),(3,5,12)])
def test_add(input1, input2, output):
	assert input1+input2 == output,"Failed"
```
Here the test method accepts 3 arguments- input1, input2, output. It adds input1 and input2 and compares against the output.  
Let's run the test by py.test -k test_add -v and see the result
```bash
test_addition.py::test_add[5-5-10] PASSED                                                                                                                                                                       
test_addition.py::test_add[3-5-12] FAILED                                                                                                                                                                                              
============================================== FAILURES ==============================================
__________________________________________ test_add[3-5-12] __________________________________________
input1 = 3, input2 = 5, output = 12
    @pytest.mark.parametrize("input1, input2, output",[(5,5,10),(3,5,12)])
    def test_add(input1, input2, output):
>   	assert input1+input2 == output,"failed"
E    AssertionError: failed
E    assert (3 + 5) == 12
test_addition.py:5: AssertionError
```
As you can see the tests ran 2 times – one checking 5+5 ==10 and other checking 3+5 ==12  
&nbsp; &nbsp; test_addition.py::test_add[5-5-10] PASSED  
&nbsp; &nbsp; test_addition.py::test_add[3-5-12] FAILED 

## XFail/ Skip tests  
There will be some situations where we don't want to execute a test, or a test case is not relevant for a particular time. In those situations, we have the option to xfail the test or skip the tests  
The xfailed test will be executed, but it will not be counted as part failed or passed tests. There will be no traceback displayed if that test fails. We can xfail tests using  
```bash
@pytest.mark.xfail
```
Skipping a test means that the test will not be executed. We can skip tests using
```bash
@pytest.mark.skip
```
## Results in XML
We can create test results in XML format which we can feed to **Continuous Integration** servers for further processing
```bash
py.test test_assert.py -v --junitxml="result.xml"
```