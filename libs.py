import pandas as pd
from analise import processar_dados_vendas
from flask import Flask, request, jsonify, render_template
import uuid
import os