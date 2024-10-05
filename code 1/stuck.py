import requests
from bs4 import BeautifulSoup

class StockScraper:
    def __init__(self, stock_symbol):
        """
        سازنده کلاس که نماد سهام را به عنوان ورودی می‌پذیرد.
        """
        self.base_url = f"https://finance.yahoo.com/quote/{stock_symbol}?p={stock_symbol}"
        self.page_content = None

    def fetch_page(self):
        """
        این متد صفحه سهام موردنظر را واکشی می‌کند.
        """
        try:
            response = requests.get(self.base_url)
            if response.status_code == 200:
                self.page_content = response.text
                print("صفحه با موفقیت واکشی شد!")
            else:
                print(f"خطا در واکشی صفحه. کد وضعیت: {response.status_code}")
        except Exception as e:
            print(f"خطا در واکشی صفحه: {e}")

    def parse_stock_data(self):
        """
        این متد داده‌های قیمت سهام و اطلاعات مرتبط را از صفحه واکشی‌شده استخراج می‌کند.
        """
        if self.page_content is None:
            print("ابتدا باید صفحه را واکشی کنید.")
            return

        soup = BeautifulSoup(self.page_content, 'html.parser')
        
        # استخراج قیمت فعلی سهام
        try:
            price = soup.find('fin-streamer', {'data-field': 'regularMarketPrice'}).text
            print(f"قیمت فعلی سهام: {price}")
        except AttributeError:
            print("قیمت سهام یافت نشد.")
        
        # استخراج تغییرات قیمت سهام
        try:
            change = soup.find('fin-streamer', {'data-field': 'regularMarketChange'}).text
            change_percent = soup.find('fin-streamer', {'data-field': 'regularMarketChangePercent'}).text
            print(f"تغییرات قیمت: {change} ({change_percent})")
        except AttributeError:
            print("تغییرات قیمت سهام یافت نشد.")

    def get_stock_data(self):
        """
        متدی که به طور کامل صفحه را واکشی کرده و داده‌های مالی را استخراج می‌کند.
        """
        self.fetch_page()
        self.parse_stock_data()


# استفاده از کلاس برای اسکرب کردن داده‌های یک سهام خاص
if __name__ == "__main__":
    # به عنوان مثال سهام شرکت اپل (AAPL)
    stock_symbol = "AAPL"  # می‌توانید این را با هر نماد سهامی جایگزین کنید
    scraper = StockScraper(stock_symbol)
    
    # دریافت داده‌های سهام
    scraper.get_stock_data()
