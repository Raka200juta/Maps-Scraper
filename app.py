from flask import Flask, render_template, request, jsonify
from scraper import scrape_gmaps

app = Flask(__name__)

# Route utama untuk Admin Panel
@app.route('/', methods=['GET', 'POST'])
def index():
    data_hasil = []
    keyword = ""
    lokasi = ""
    
    if request.method == 'POST':
        keyword = request.form.get('keyword')
        provinsi = request.form.get('provinsi')
        kota = request.form.get('kota')
        
        # Gabungkan filter wilayah untuk query pencarian
        lokasi = f"{kota}, {provinsi}" if kota else provinsi
        
        # Jalankan fungsi scraper
        data_hasil = scrape_gmaps(keyword, lokasi)
        
    return render_template('index.html', results=data_hasil, keyword=keyword, lokasi=lokasi)

if __name__ == '__main__':
    app.run(debug=True, port=5000)