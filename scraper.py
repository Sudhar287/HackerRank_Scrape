import os
from getpass import getpass
import time
import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import exceptions  

def get_credentials():
	email = input('Please enter your HackerRank username or email address \n')
	password = getpass('Please enter your HackerRank password \n')
	print ('Thank you')
	return email, password


class Scraper():

	def __init__(self,email,password):
		self.email = email
		self.password = password
		self.accessor = tk.Tk()
		# Insert the location of your browser driver below.
		self.browser = webdriver.Chrome('/home/sudharshann/Documents/chromedriver')

	def login(self):
		self.browser.get('https://www.hackerrank.com/dashboard')

		elem = self.browser.find_element_by_xpath('//button[normalize-space()="Log In"]')
		elem.click()

		loginbar = self.browser.find_element_by_id("input-1")
		loginbar.send_keys(self.email)

		passwordbar = self.browser.find_element_by_id("input-2")
		passwordbar.send_keys(self.password)

		remebermebutton= self.browser.find_element_by_css_selector("input.checkbox-input")
		remebermebutton.click()


		loginbutton= self.browser.find_element_by_css_selector("button.ui-btn.ui-btn-large.ui-btn-primary.auth-button")
		loginbutton.click()

		time.sleep(0.5)

	def go_to_submissions(self):

		profilebutton = self.browser.find_element_by_css_selector("span.mmR.username.text-ellipsis")
		profilebutton.click()

		time.sleep(0.5)

		subs = self.browser.find_element_by_partial_link_text("Submissions")
		subs.click()

		time.sleep(0.5)

	def navigate_and_download(self):
		
		langauges_dict={'Java 7':'java','C++':'cpp','MySQL':'sql','C++14':'cpp','C':'c',\
					 'Python 3':'py', 'Scala':'scala', 'Oracle':'oracle'}

		for i in range(1,32):
			current_page_url = "https://www.hackerrank.com/submissions/all/page/%d" % i
			print (current_page_url)
			self.browser.get(current_page_url)
			time.sleep(0.5)
			for j in range(0,10):
				print (current_page_url,j)
				list_subs = self.browser.find_elements_by_css_selector("a.challenge-slug.backbone.root")
				list_subs_lang = self.browser.find_elements_by_css_selector("p.small")
				particular_sub_driver = list_subs[j]
				particular_sub_lang_driver = list_subs_lang[4*j]
				challege_name = particular_sub_driver.text
				lang_coded_in = particular_sub_lang_driver.text
				print (challege_name,lang_coded_in)
				save_file_name = challege_name + '.' + langauges_dict[lang_coded_in]
				try: 
					particular_sub_driver.click()
					challege_tabs = self.browser.find_elements_by_css_selector("span.ui-icon-label")
					time.sleep(0.5)
					subs_tab = challege_tabs[1]
					time.sleep(0.5)
					subs_tab.click()
					time.sleep(0.5)
					view_results= self.browser.find_element_by_css_selector('a.text-link')
					time.sleep(0.5)
					view_results.click()

					time.sleep(1)

					if ((len(self.browser.find_elements_by_css_selector("span.cm-keyword"))) != 0):
						text_box = self.browser.find_element_by_css_selector("span.cm-keyword")
					elif ((len(self.browser.find_elements_by_css_selector("span.cm-variable"))) != 0):
						text_box = self.browser.find_element_by_css_selector("span.cm-variable")
					elif ((len(browser.find_elements_by_css_selector("span.cm-meta"))) != 0):
						text_box = self.browser.find_element_by_css_selector("span.cm-meta")

					
					time.sleep(0.5)
					actions = ActionChains(self.browser)
					actions.move_to_element(text_box)
					actions.click()
					actions.key_down(Keys.LEFT_CONTROL).send_keys("a").key_up(Keys.LEFT_CONTROL)
					actions.key_down(Keys.LEFT_CONTROL).send_keys("c").key_up(Keys.LEFT_CONTROL)
					actions.perform()

					code = None
					while code is None:	
						try:
							code = self.accessor.clipboard_get()
						except tk.TclError:
							print ('Tkinter TclError. Please contact the author.')
							exit()

				except (exceptions.StaleElementReferenceException):
					print ('Selenium StaleElementReferenceException. Please contact the author.')
					continue;

				lang_specific_dir = './results/' + langauges_dict[lang_coded_in]
				if not os.path.exists(lang_specific_dir):
					os.mkdir(lang_specific_dir)
				text_file = open(lang_specific_dir +'/'+ save_file_name,'w')
				text_file.write(code)
				text_file.close()
				print ('Success')

				self.browser.get(current_page_url)
				time.sleep(0.5)

if __name__ == "__main__":

	print ('---------START---------')

	if not os.path.exists('./results'):
		os.mkdir('./results')

	email, password = get_credentials()

	instance = Scraper(email,password)
	instance.login()
	instance.go_to_submissions()
	instance.navigate_and_download()

	print ('---------DONE---------')
