"""
Praktikum Rule-Based Methods for Probabilistic Reasoning
Sistem Pakar Diagnosis Penyakit Kulit menggunakan Certainty Factor (CF)
Mata Kuliah: Kecerdasan Buatan
Institut Teknologi Del
"""

# ============================================================================
# LANGKAH 2: DEFINISI BASIS PENGETAHUAN (KNOWLEDGE BASE)
# ============================================================================

# 1. Definisikan Gejala (Evidence)
gejala = {
    'G01': 'Ruam Kulit Kemerahan',
    'G02': 'Gatal',
    'G03': 'Tekstur kulit kering',
    'G04': 'Adanya pembengkakan',
    'G05': 'Kulit bersisik',
    'G06': 'Kulit melepuh',
    'G07': 'Penebalan pada kulit',
    'G08': 'Kulit pecah-pecah',
    'G09': 'Kulit terasa nyeri atau sakit',
    'G10': 'Penyakit dapat menyebar',
    'G11': 'Luka yang mengeluarkan cairan',
    'G12': 'Bentuk ruam tidak beraturan',
    'G13': 'Adanya bercak putih, coklat, merah',
    'G14': 'Terdapat bintil-bintil kecil',
    'G15': 'Bentuk melingkar seperti cincin',
    'G16': 'Demam',
    'G17': 'Pilek',
    'G18': 'Cepat merasa lelah',
    'G19': 'Nyeri sendi',
    'G20': 'Pusing dan sakit kepala',
    'G21': 'Kulit menjadi sensitif'
}

# 2. Definisikan Penyakit (Hipotesis)
penyakit = {
    'P01': 'Dermatitis Alergi',
    'P02': 'Dermatitis Atopik',
    'P03': 'Urtikaria',
    'P04': 'Panu',
    'P05': 'Tinea/Kurap',
    'P06': 'Herpes Zooster',
    'P07': 'Biang Keringat'
}

# 3. Definisikan Aturan (Rules)
rules = {
    'P01': ['G01', 'G02', 'G03', 'G04', 'G05', 'G06', 'G07', 'G08', 'G09', 'G11'],
    'P02': ['G01', 'G02', 'G03', 'G04', 'G05', 'G06', 'G09', 'G10', 'G11'],
    'P03': ['G01', 'G02', 'G07', 'G09', 'G10', 'G12'],
    'P04': ['G02', 'G05', 'G10', 'G13'],
    'P05': ['G02', 'G05', 'G14', 'G15'],
    'P06': ['G06', 'G09', 'G11', 'G16', 'G17', 'G18', 'G19', 'G20', 'G21'],
    'P07': ['G01', 'G02', 'G14']
}

# 4. Definisikan Bobot MB dan MD
cf_weights = {
    # Dermatitis Alergi (P01)
    ('P01', 'G01'): (0.8, 0.2),
    ('P01', 'G02'): (0.6, 0.4),
    ('P01', 'G03'): (0.8, 0.2),
    ('P01', 'G04'): (0.4, 0.6),
    ('P01', 'G05'): (0.6, 0.4),
    ('P01', 'G06'): (0.2, 0.8),
    ('P01', 'G07'): (0.4, 0.6),
    ('P01', 'G08'): (0.4, 0.6),
    ('P01', 'G09'): (0.6, 0.4),
    ('P01', 'G11'): (0.4, 0.6),
    
    # Dermatitis Atopik (P02) - DILENGKAPI
    ('P02', 'G01'): (0.8, 0.2),
    ('P02', 'G02'): (0.8, 0.2),
    ('P02', 'G03'): (0.8, 0.2),
    ('P02', 'G04'): (0.6, 0.4),
    ('P02', 'G05'): (0.8, 0.2),
    ('P02', 'G06'): (0.4, 0.6),
    ('P02', 'G09'): (0.6, 0.4),
    ('P02', 'G10'): (0.6, 0.4),
    ('P02', 'G11'): (0.6, 0.4),
    
    # Urtikaria (P03)
    ('P03', 'G01'): (0.8, 0.2),
    ('P03', 'G02'): (0.8, 0.2),
    ('P03', 'G07'): (0.8, 0.2),
    ('P03', 'G09'): (0.4, 0.6),
    ('P03', 'G10'): (0.8, 0.2),
    ('P03', 'G12'): (0.6, 0.4),
    
    # Panu (P04)
    ('P04', 'G02'): (0.8, 0.2),
    ('P04', 'G05'): (0.8, 0.2),
    ('P04', 'G10'): (0.6, 0.4),
    ('P04', 'G13'): (0.8, 0.2),
    
    # Tinea/Kurap (P05)
    ('P05', 'G02'): (0.8, 0.2),
    ('P05', 'G05'): (0.8, 0.2),
    ('P05', 'G14'): (0.4, 0.6),
    ('P05', 'G15'): (0.8, 0.2),
    
    # Herpes Zooster (P06) - DILENGKAPI
    ('P06', 'G06'): (0.8, 0.2),
    ('P06', 'G09'): (0.8, 0.2),
    ('P06', 'G11'): (0.6, 0.4),
    ('P06', 'G16'): (0.6, 0.4),
    ('P06', 'G17'): (0.4, 0.6),
    ('P06', 'G18'): (0.6, 0.4),
    ('P06', 'G19'): (0.6, 0.4),
    ('P06', 'G20'): (0.4, 0.6),
    ('P06', 'G21'): (0.8, 0.2),
    
    # Biang Keringat (P07)
    ('P07', 'G01'): (0.6, 0.4),
    ('P07', 'G02'): (0.8, 0.2),
    ('P07', 'G14'): (0.8, 0.2),
}

# ============================================================================
# LANGKAH 3: IMPLEMENTASI FUNGSI CERTAINTY FACTOR
# ============================================================================

def calculate_cf(mb, md):
    """
    Menghitung CF tunggal dari MB dan MD.
    
    Formula: CF = MB - MD
    
    Args:
        mb (float): Measure of Belief (0-1)
        md (float): Measure of Disbelief (0-1)
    
    Returns:
        float: Nilai Certainty Factor (-1 sampai +1)
    """
    return mb - md


def combine_cf(cf1, cf2):
    """
    Mengkombinasikan dua nilai CF.
    
    Formula berbeda tergantung tanda CF:
    - Jika keduanya positif: CF1 + CF2 * (1 - CF1)
    - Jika keduanya negatif: CF1 + CF2 * (1 + CF1)
    - Jika berbeda tanda: (CF1 + CF2) / (1 - min(|CF1|, |CF2|))
    
    Args:
        cf1 (float): Certainty Factor pertama
        cf2 (float): Certainty Factor kedua
    
    Returns:
        float: Nilai CF hasil kombinasi
    """
    if cf1 >= 0 and cf2 >= 0:
        # Keduanya positif
        return cf1 + cf2 * (1 - cf1)
    elif cf1 < 0 and cf2 < 0:
        # Keduanya negatif
        return cf1 + cf2 * (1 + cf1)
    else:
        # Berbeda tanda
        return (cf1 + cf2) / (1 - min(abs(cf1), abs(cf2)))


# ============================================================================
# LANGKAH 4: MESIN INFERENSI (INFERENCE ENGINE)
# ============================================================================

def run_inference(gejala_pasien, verbose=False):
    """
    Menjalankan mesin inferensi untuk menghitung CF setiap penyakit
    berdasarkan gejala yang dialami pasien.
    
    Args:
        gejala_pasien (list): Daftar kode gejala yang dialami pasien
        verbose (bool): Jika True, tampilkan detail perhitungan
    
    Returns:
        list: Daftar tuple (nama_penyakit, cf_final) terurut dari tertinggi
    """
    hasil_diagnosis = {}
    detail_perhitungan = {}
    
    # Iterasi setiap penyakit dalam basis pengetahuan
    for kode_penyakit, nama_penyakit in penyakit.items():
        # Dapatkan daftar gejala yang relevan untuk penyakit ini
        gejala_relevan = rules.get(kode_penyakit, [])
        
        # Filter gejala pasien yang sesuai dengan aturan penyakit ini
        gejala_cocok = [g for g in gejala_pasien if g in gejala_relevan]
        
        if not gejala_cocok:
            continue  # Tidak ada gejala yang cocok
        
        # Hitung CF untuk setiap gejala yang cocok
        cf_list = []
        detail_gejala = []
        
        for g in gejala_cocok:
            mb, md = cf_weights.get((kode_penyakit, g), (0, 0))
            if mb + md > 0:  # Pastikan ada bobotnya
                cf = calculate_cf(mb, md)
                cf_list.append(cf)
                detail_gejala.append({
                    'gejala': g,
                    'nama': gejala[g],
                    'mb': mb,
                    'md': md,
                    'cf': cf
                })
        
        if not cf_list:
            continue
        
        # Kombinasikan CF
        cf_final = cf_list[0]
        kombinasi_steps = [cf_list[0]]
        
        for i in range(1, len(cf_list)):
            cf_final = combine_cf(cf_final, cf_list[i])
            kombinasi_steps.append(cf_final)
        
        hasil_diagnosis[nama_penyakit] = cf_final
        detail_perhitungan[nama_penyakit] = {
            'gejala_cocok': detail_gejala,
            'cf_list': cf_list,
            'kombinasi_steps': kombinasi_steps,
            'cf_final': cf_final
        }
    
    # Urutkan hasil dari CF tertinggi ke terendah
    hasil_urut = sorted(hasil_diagnosis.items(), key=lambda item: item[1], reverse=True)
    
    # Tampilkan detail jika verbose
    if verbose:
        for nama, detail in sorted(detail_perhitungan.items(), 
                                   key=lambda x: x[1]['cf_final'], 
                                   reverse=True):
            print(f"\n{'='*70}")
            print(f"PENYAKIT: {nama}")
            print(f"{'='*70}")
            print(f"\nGejala yang cocok:")
            for gej in detail['gejala_cocok']:
                print(f"  {gej['gejala']}: {gej['nama']}")
                print(f"    MB={gej['mb']}, MD={gej['md']}, CF={gej['cf']:.3f}")
            
            print(f"\nProses Kombinasi CF:")
            for i, cf_val in enumerate(detail['kombinasi_steps']):
                if i == 0:
                    print(f"  CF awal = {cf_val:.4f}")
                else:
                    print(f"  CF ke-{i+1} = {cf_val:.4f}")
            
            print(f"\nCF FINAL: {detail['cf_final']:.4f} ({detail['cf_final']*100:.2f}%)")
    
    return hasil_urut


def tampilkan_hasil(hasil, judul="Hasil Diagnosis"):
    """
    Menampilkan hasil diagnosis dengan format yang rapi.
    
    Args:
        hasil (list): List hasil dari run_inference
        judul (str): Judul untuk ditampilkan
    """
    print(f"\n{'='*70}")
    print(f"{judul:^70}")
    print(f"{'='*70}")
    
    if not hasil:
        print("Tidak ada diagnosis yang cocok dengan gejala yang diberikan.")
        return
    
    print(f"{'No.':<5} {'Penyakit':<30} {'CF':<15} {'Persentase'}")
    print(f"{'-'*70}")
    
    for idx, (penyakit_nama, cf) in enumerate(hasil, 1):
        print(f"{idx:<5} {penyakit_nama:<30} {cf:<15.4f} {cf*100:.2f}%")
    
    print(f"{'='*70}")
    print(f"Diagnosis Tertinggi: {hasil[0][0]} ({hasil[0][1]*100:.2f}%)")
    print(f"{'='*70}\n")


# ============================================================================
# LANGKAH 5 & TUGAS 2-4: UJI COBA PROGRAM
# ============================================================================

print("="*70)
print("SISTEM PAKAR DIAGNOSIS PENYAKIT KULIT")
print("Menggunakan Metode Certainty Factor (CF)")
print("="*70)

# ============================================================================
# UJI KASUS 1: RESPONDEN 179
# ============================================================================
print("\n" + "="*70)
print("UJI KASUS 1: RESPONDEN 179")
print("="*70)

input_179 = ['G02', 'G05', 'G01', 'G15']
print("\nGejala yang dialami:")
for g in input_179:
    print(f"  - {g}: {gejala[g]}")

hasil_179 = run_inference(input_179, verbose=True)
tampilkan_hasil(hasil_179, "Hasil Diagnosis Responden 179")

# Perhitungan Manual untuk Verifikasi
print("\nVERIFIKASI PERHITUNGAN MANUAL (Tinea/Kurap):")
print("Gejala yang cocok dengan P05: G02, G05, G15")
print("  CF(G02) = 0.8 - 0.2 = 0.6")
print("  CF(G05) = 0.8 - 0.2 = 0.6")
print("  CF(G15) = 0.8 - 0.2 = 0.6")
print("\nKombinasi:")
cf1 = 0.6
cf2 = 0.6
cf_combined_1 = cf1 + cf2 * (1 - cf1)
print(f"  CF_combine(0.6, 0.6) = 0.6 + 0.6*(1-0.6) = {cf_combined_1:.4f}")
cf3 = 0.6
cf_final_manual = cf_combined_1 + cf3 * (1 - cf_combined_1)
print(f"  CF_combine({cf_combined_1:.4f}, 0.6) = {cf_final_manual:.4f} = {cf_final_manual*100:.2f}%")

# ============================================================================
# UJI KASUS 2: RESPONDEN 137
# ============================================================================
print("\n" + "="*70)
print("UJI KASUS 2: RESPONDEN 137")
print("="*70)

input_137 = ['G02', 'G05', 'G11', 'G01', 'G03', 'G06', 'G07', 'G08', 'G09', 'G04']
print("\nGejala yang dialami:")
for g in input_137:
    print(f"  - {g}: {gejala[g]}")

hasil_137 = run_inference(input_137, verbose=True)
tampilkan_hasil(hasil_137, "Hasil Diagnosis Responden 137")

# ============================================================================
# UJI KASUS 3: RESPONDEN 144
# ============================================================================
print("\n" + "="*70)
print("UJI KASUS 3: RESPONDEN 144")
print("="*70)

input_144 = ['G02', 'G01', 'G07', 'G09', 'G10', 'G13']
print("\nGejala yang dialami:")
for g in input_144:
    print(f"  - {g}: {gejala[g]}")

hasil_144 = run_inference(input_144, verbose=True)
tampilkan_hasil(hasil_144, "Hasil Diagnosis Responden 144")

# ============================================================================
# RINGKASAN HASIL SEMUA RESPONDEN
# ============================================================================
print("\n" + "="*70)
print("RINGKASAN HASIL SEMUA RESPONDEN")
print("="*70)

print(f"\n{'Responden':<15} {'Diagnosis CF Tertinggi':<30} {'CF (%)':<15}")
print("-"*70)
print(f"{'179':<15} {hasil_179[0][0]:<30} {hasil_179[0][1]*100:.2f}%")
print(f"{'137':<15} {hasil_137[0][0]:<30} {hasil_137[0][1]*100:.2f}%")
print(f"{'144':<15} {hasil_144[0][0]:<30} {hasil_144[0][1]*100:.2f}%")
print("="*70)