# Vamos gerar o arquivo dicionario.json completo para que o usuário possa baixá-lo ou copiá-lo facilmente
import json
import pandas as pd

df_raw = pd.read_csv('Organização Carneniana de Línguas (OCL) - Língua Lírica-Carneniana - DICIONARIO.csv', header=None)
main_dict = df_raw.iloc[2:, :7].copy()
main_dict.columns = ['singular', 'traducao', 'classe', 'plural', 'pronuncia', 'uso', 'ambiente']
main_dict = main_dict.dropna(subset=['singular'])

records = []
for _, row in main_dict.iterrows():
    sing = str(row['singular']).strip() if pd.notna(row['singular']) else ""
    if not sing or sing.lower() == 'nan':
        continue
    trad = str(row['traducao']).strip() if pd.notna(row['traducao']) else ""
    cls = str(row['classe']).strip() if pd.notna(row['classe']) else ""
    plur = str(row['plural']).strip() if pd.notna(row['plural']) and str(row['plural']).strip() != 'nan' else "-"
    pron = str(row['pronuncia']).strip() if pd.notna(row['pronuncia']) and str(row['pronuncia']).strip() != 'nan' else ""
    uso = str(row['uso']).strip() if pd.notna(row['uso']) and str(row['uso']).strip() != 'nan' else ""
    amb = str(row['ambiente']).strip() if pd.notna(row['ambiente']) and str(row['ambiente']).strip() != 'nan' else ""
    
    records.append({
        "singular": sing,
        "traducao": trad,
        "classe": cls,
        "plural": plur,
        "pronuncia": pron,
        "uso": uso,
        "ambiente": amb
    })

with open('dicionario.json', 'w', encoding='utf-8') as f:
    json.dump(records, f, ensure_ascii=False, indent=2)

print(f"Arquivo dicionario.json gerado com sucesso com {len(records)} termos!")