from rufus.synthesizer import ContentSynthesizer

def test_synthesize_to_json(tmp_path):
    data = {"https://quotes.toscrape.com/": "Example content"}
    output_path = tmp_path / "output.json"
    synthesizer = ContentSynthesizer()
    synthesizer.synthesize_to_json(data, str(output_path))
    assert output_path.exists()

def test_synthesize_to_csv(tmp_path):
    data = {"https://quotes.toscrape.com/": "Example content"}
    output_path = tmp_path / "output.csv"
    synthesizer = ContentSynthesizer()
    synthesizer.synthesize_to_csv(data, str(output_path))
    assert output_path.exists()

def test_filter_relevant_content():
    synthesizer = ContentSynthesizer()
    data = {
        "https://quotes.toscrape.com/": "This page contains FAQs about our product.",
        "https://irrelevant.com": "Unrelated content here."
    }
    prompt = "FAQs"
    filtered = synthesizer.filter_relevant_content(data, prompt)
    assert len(filtered) == 1
    assert "https://quotes.toscrape.com/" in filtered
