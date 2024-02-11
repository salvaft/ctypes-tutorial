
CC := gcc
CFLAGS := -Wall -fPIC

SRC_DIR := c_libs
BUILD_DIR := c_libs/build

SRC_FILES := $(wildcard $(SRC_DIR)/*.c)
SO_FILES := $(patsubst $(SRC_DIR)/%.c,$(BUILD_DIR)/%.so,$(SRC_FILES))
TEST_FILES := $(wildcard $(SRC_DIR)/tests/test_*.py)
TEST_DIR := tests

all: $(SO_FILES)

$(BUILD_DIR)/%.so: $(SRC_DIR)/%.c | $(BUILD_DIR)
	@$(CC) $(CFLAGS) -shared -o $@ $<

$(BUILD_DIR):
	@mkdir -p $(BUILD_DIR)

clean:
	rm -rf $(BUILD_DIR)

run: all
	@python -m src.$(chapter).$(exercise)

test: all
	# python -m unittest discover -s $(TEST_DIR) -p 'test_*.py'
	poetry run pytest $(TEST_DIR)

.PHONY: lint type-check format build

lint:
	poetry run pylint **/*.py

format:
	poetry run black .


.PHONY: all clean test lint types format
