# T3AIHackathon-FineTuning
Bu proje TEKNOFEST 2024 Antalya T3AI Hackathon Yarışması İnce Ayarlama Kategorisi için geliştirilmiştir

## TRT Data Warriors: 563707
- İlknur Durgar Elkahlout
- Mustafa Budak
- Muhammet Nusret Özateş
- Muhammed Lutfi Türkcan
- Muhammed Emir Koçak

## Veri Seti Kaynaklari

### Türk Eğitim Sistemi
- [MEB](https://www.meb.gov.tr/)
- [Hugging Face](https://huggingface.co/datasets/alibayram/turkish_mmlu)

### Türk Hukuku
- [Mevzuat](https://www.mevzuat.gov.tr/)
### Sürdürülebilirlik

- [WIKIPEDIA]https://tr.wikipedia.org/wiki/S%C3%BCrd%C3%BCr%C3%BClebilirlik
- [CarbonGate]https://www.carbongate.io/blog/surdurulebilirlik-raporu-hazirlama-adim-adim-kilavuz
- [MFA]https://www.mfa.gov.tr/surdurulebilir-kalkinma.tr.mfa
- [satinalmadergisi]https://satinalmadergisi.com/surdurulebilirlik-okulu-test-2/
- [satinalmadergisi]https://satinalmadergisi.com/surdurulebilirlik-sinav-sorulari-surdurulebilirlik-okulu/
- [Hugging Face]https://huggingface.co/datasets/alibayram/turkish_mmlu

### Tarım
- [Tarım ve Orman Bakanlığı](https://www.tarimorman.gov.tr/)
- [Hugging Face](https://huggingface.co/datasets/alibayram/turkish_mmlu)
- [TGDF](https://www.tgdf.org.tr/)

## Ince Ayarlama Sürecini Başlatma
```bash
llamafactory-cli train llama3_config.yaml
```

## Sınama Görevi: Fonksiyon Çağırma

```bash
streamlit run function_call_ui.py
```
