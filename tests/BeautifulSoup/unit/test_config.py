import pytest
from utilities.config import JSONConfig
import copy


@pytest.mark.parametrize("no_brokers_config", [{"brokers": []}])
def test_count(no_brokers_config):
    with pytest.raises(Exception) as e:
        JSONConfig("brokers", no_brokers_config).check()
    assert "No brokers found in json file" in str(e.value)


@pytest.mark.usefixtures("config")
def test_good_configs(config):
    JSONConfig("brokers", config).check()

    more_than_one_broker = copy.deepcopy(config)
    more_than_one_broker["brokers"].append(config["brokers"][0])
    assert len(more_than_one_broker["brokers"]) > 1
    JSONConfig("brokers", more_than_one_broker).check()


@pytest.mark.usefixtures("config")
def test_missing_field(config):
    bad_config = copy.deepcopy(config)
    bad_config["brokers"][0].pop("domain_name")
    with pytest.raises(Exception) as e:
        JSONConfig("brokers", bad_config).check()
    assert "Missing field 'domain_name' in config" in str(e.value)

    bad_config = copy.deepcopy(config)
    bad_config["brokers"][0].pop("url_filter")
    with pytest.raises(Exception) as e:
        JSONConfig("brokers", bad_config).check()
    assert "Missing field 'url_filter' in config" in str(e.value)

    bad_config = copy.deepcopy(config)
    bad_config["brokers"][0].pop("property_translations")
    with pytest.raises(Exception) as e:
        JSONConfig("brokers", bad_config).check()
    assert "Missing field 'property_translations' in config" in str(e.value)

    bad_config = copy.deepcopy(config)
    bad_config["brokers"].append(config["brokers"][0])
    assert len(bad_config["brokers"]) > 1
    bad_config["brokers"][1].pop("property_translations")
    with pytest.raises(Exception) as e:
        JSONConfig("brokers", bad_config).check()
    assert "Missing field 'property_translations' in config" in str(e.value)


@pytest.mark.usefixtures("config")
def test_missing_subfield(config):
    bad_config = copy.deepcopy(config)
    bad_config["brokers"][0]["property_filters"].pop("property_value_filter")
    with pytest.raises(Exception) as e:
        JSONConfig("brokers", bad_config).check()
    assert "Missing subfield(s) under 'property_filters' in config" in str(e.value)

    bad_config = copy.deepcopy(config)
    bad_config["brokers"][0]["property_translations"].pop("rent")
    with pytest.raises(Exception) as e:
        JSONConfig("brokers", bad_config).check()
    assert "Missing subfield(s) under 'property_translations' in config" in str(e.value)

    bad_config = copy.deepcopy(config)
    bad_config["brokers"].append(config["brokers"][0])
    assert len(bad_config["brokers"]) > 1
    bad_config["brokers"][1]["property_translations"].pop("rent")
    with pytest.raises(Exception) as e:
        JSONConfig("brokers", bad_config).check()
    assert "Missing subfield(s) under 'property_translations' in config" in str(e.value)
