import unittest
from selenium import webdriver
import time
class TestOne(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.PhantomJS()
		self.driver.set_window_size(1120, 550)

	def test_url(self):
		self.driver.get("http://jobs.kent.edu/cw/en-us/listing/")
		self.driver.find_element_by_id('search-keyword').send_keys("chemistry")
		time.sleep(3)		
		self.assertIn("http://jobs.kent.edu/cw/en-us/search/?search-keyword=chemistry", self.driver.current_url)
		tdata = self.driver.find_element_by_id("search-results-content")
		tvalues = tdata.find_elements_by_tag_name("td")
		print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")		
		for i in tvalues[0:5]:
			print(i.text)
		print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
		for i in tvalues[6:11]:
			print(i.text)
		print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
		
			
        #tabledata = self.driver.find_element_by_id("search-results-content")

	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()