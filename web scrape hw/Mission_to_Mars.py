{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Setting up\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "#import BeautifulSoup\n",
    "from bs4 import BeautifulSoup\n",
    "from splinter import Browser"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Set the executable path and initilalize the chrome browser\n",
    "executable_path = {'executable_path': '/usr/local/bin/chromedriver'}\n",
    "browser = Browser('chrome', **executable_path)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Visit the NAA Mars News Sites"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit the Mars Nasa news site\n",
    "url = 'https://mars.nasa.gov/news/'\n",
    "browser.visit(url)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "html = browser.html\n",
    "\n",
    "news_soup = BeautifulSoup(html, 'html.parser')\n",
    "#print(news_soup)\n",
    "\n",
    "# slide element everything in the <ul class=\"item_list\">\n",
    "# <li class='slide'>\n",
    "# ....\n",
    "# </ul>\n",
    "slide_element = news_soup.select_one('ul.item_list li.slide')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<div class=\"content_title\"><a href=\"/news/8433/for-insight-dust-cleanings-will-yield-new-science/\" target=\"_self\">For InSight, Dust Cleanings Will Yield New Science</a></div>"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "slide_element.find(\"div\", class_= \"content_title\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'For InSight, Dust Cleanings Will Yield New Science'"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# use the parent element to find the first a tag and save it as news_title\n",
    "news_title = slide_element.find(\"div\", class_=\"content_title\").get_text()\n",
    "news_title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Wind can be crucial to clearing dust from spacecraft solar panels on Mars. With InSight\\'s meteorological sensors, scientists get their first measurements of wind and dust interacting \"live\" on the Martian surface.  '"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "news_paragraph= slide_element.find('div', class_=\"article_teaser_body\").get_text()\n",
    "news_paragraph"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## JPL Space Images Featured Image\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {'executable_path': '/usr/local/bin/chromedriver'}\n",
    "browser = Browser('chrome', **executable_path)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit URK\n",
    "url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'\n",
    "browser.visit(url)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "# asking Splinter to go to site and hit button with a class name full_image\n",
    "# <button class=\"full_image\"> Full Image</button>\n",
    "\n",
    "full_image_button = browser.find_by_id('full_image')\n",
    "full_image_button.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Find the more info button and click on that \n",
    "browser.is_element_present_by_text('more info', wait_time= 1)\n",
    "more_info_element = browser.find_link_by_partial_text('more info')\n",
    "more_info_element.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "#parse the results html with soup\n",
    "html = browser.html\n",
    "image_soup = BeautifulSoup(html,'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'/spaceimages/images/largesize/PIA18847_hires.jpg'"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "img_url = image_soup.select_one('figure.lede a img').get('src')\n",
    "img_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://www.jps.nasa.govhttps://www.jps.nasa.gov/spaceimages/images/largesize/PIA18847_hires.jpg'"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#use the base url to create an absolute url \n",
    "img_url = f'https://www.jps.nasa.gov{img_url}'\n",
    "img_url"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## MARS WEATHER"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = \"https://twitter.com/marswxreport?lang=en\"\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "html= browser.html\n",
    "weather_soup = BeautifulSoup(html, 'html.parser')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [],
   "source": [
    "# first find a tweet with the data-name 'Mars Weather'\n",
    "mars_weather_tweet = weather_soup.find('div', \n",
    "                                 attrs={\n",
    "                                     \"class\": \"tweet\",\n",
    "                                     \"data-name\": \"Mars Weather\"\n",
    "                                 })\n",
    "\n",
    "# print(mars_weather_tweet)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'InSight sol 158 (2019-05-07) low -99.7ºC (-147.5ºF) high -21.8ºC (-7.2ºF)\\nwinds from the SSE at 4.8 m/s (10.7 mph) gusting to 13.6 m/s (30.4 mph)\\npressure at 7.50 hPapic.twitter.com/8SrPjAhpGZ'"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#next seach within tweet for p tag containing the tweet text\n",
    "mars_weather = mars_weather_tweet.find('p','tweet-text').get_text()\n",
    "mars_weather\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "hemisphere_image_urls = []\n",
    "\n",
    "# First get a list og all the hemispheres\n",
    "links =browser.find_by_css('a.product-item h3')\n",
    "for item in range(len(links)):\n",
    "    hemisphere = {}\n",
    "    \n",
    "    # we have to find the element on each loop to avoid stale element exceptcion \n",
    "    browser.find_by_css('a.product-item h3')[item].click()\n",
    "    \n",
    "    # next we find the sample image anchor tag and extract the hred\n",
    "    sample_element = browser.find_link_by_text('Sample').first\n",
    "    hemisphere['img_url'] = sample_element['href']\n",
    "    \n",
    "    # get the hemisphere title\n",
    "    hemisphere['title'] = browser.find_by_css('h2.title').text\n",
    "    \n",
    "    # append hemisphere object to a list\n",
    "    hemisphere_image_urls.append(hemisphere)\n",
    "    \n",
    "    # finally, we navigate backwards\n",
    "    browser.back()\n",
    "    \n",
    "    \n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg',\n",
       "  'title': 'Cerberus Hemisphere Enhanced'},\n",
       " {'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg',\n",
       "  'title': 'Schiaparelli Hemisphere Enhanced'},\n",
       " {'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg',\n",
       "  'title': 'Syrtis Major Hemisphere Enhanced'},\n",
       " {'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg',\n",
       "  'title': 'Valles Marineris Hemisphere Enhanced'}]"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hemisphere_image_urls"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## MARS FACTS"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                      0                              1\n",
      "0  Equatorial Diameter:                       6,792 km\n",
      "1       Polar Diameter:                       6,752 km\n",
      "2                 Mass:  6.42 x 10^23 kg (10.7% Earth)\n",
      "3                Moons:            2 (Phobos & Deimos)\n",
      "4       Orbit Distance:       227,943,824 km (1.52 AU)\n",
      "5         Orbit Period:           687 days (1.9 years)\n",
      "6  Surface Temperature:                  -153 to 20 °C\n",
      "7         First Record:              2nd millennium BC\n",
      "8          Recorded By:           Egyptian astronomers\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>value</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>description</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Equatorial Diameter:</th>\n",
       "      <td>6,792 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Polar Diameter:</th>\n",
       "      <td>6,752 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mass:</th>\n",
       "      <td>6.42 x 10^23 kg (10.7% Earth)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Moons:</th>\n",
       "      <td>2 (Phobos &amp; Deimos)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Orbit Distance:</th>\n",
       "      <td>227,943,824 km (1.52 AU)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Orbit Period:</th>\n",
       "      <td>687 days (1.9 years)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Surface Temperature:</th>\n",
       "      <td>-153 to 20 °C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>First Record:</th>\n",
       "      <td>2nd millennium BC</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Recorded By:</th>\n",
       "      <td>Egyptian astronomers</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                              value\n",
       "description                                        \n",
       "Equatorial Diameter:                       6,792 km\n",
       "Polar Diameter:                            6,752 km\n",
       "Mass:                 6.42 x 10^23 kg (10.7% Earth)\n",
       "Moons:                          2 (Phobos & Deimos)\n",
       "Orbit Distance:            227,943,824 km (1.52 AU)\n",
       "Orbit Period:                  687 days (1.9 years)\n",
       "Surface Temperature:                  -153 to 20 °C\n",
       "First Record:                     2nd millennium BC\n",
       "Recorded By:                   Egyptian astronomers"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd \n",
    "df = pd.read_html('https://space-facts.com/mars/')[0]\n",
    "print(df)\n",
    "df.columns=['description', 'value']\n",
    "df.set_index('description', inplace=True)\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'<table border=\"1\" class=\"dataframe\">\\n  <thead>\\n    <tr style=\"text-align: right;\">\\n      <th></th>\\n      <th>value</th>\\n    </tr>\\n    <tr>\\n      <th>description</th>\\n      <th></th>\\n    </tr>\\n  </thead>\\n  <tbody>\\n    <tr>\\n      <th>Equatorial Diameter:</th>\\n      <td>6,792 km</td>\\n    </tr>\\n    <tr>\\n      <th>Polar Diameter:</th>\\n      <td>6,752 km</td>\\n    </tr>\\n    <tr>\\n      <th>Mass:</th>\\n      <td>6.42 x 10^23 kg (10.7% Earth)</td>\\n    </tr>\\n    <tr>\\n      <th>Moons:</th>\\n      <td>2 (Phobos &amp; Deimos)</td>\\n    </tr>\\n    <tr>\\n      <th>Orbit Distance:</th>\\n      <td>227,943,824 km (1.52 AU)</td>\\n    </tr>\\n    <tr>\\n      <th>Orbit Period:</th>\\n      <td>687 days (1.9 years)</td>\\n    </tr>\\n    <tr>\\n      <th>Surface Temperature:</th>\\n      <td>-153 to 20 °C</td>\\n    </tr>\\n    <tr>\\n      <th>First Record:</th>\\n      <td>2nd millennium BC</td>\\n    </tr>\\n    <tr>\\n      <th>Recorded By:</th>\\n      <td>Egyptian astronomers</td>\\n    </tr>\\n  </tbody>\\n</table>'"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.to_html()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
