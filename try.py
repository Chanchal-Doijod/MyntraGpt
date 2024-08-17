from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-recommendations', methods=['POST'])
def get_recommendations():
    try:
        data = request.get_json()
        print("Received data:", data)
        
        if not data or 'responses' not in data:
            return jsonify({'error': 'Invalid data'}), 400

        responses = data['responses']
        print("Processed responses:", responses)

        # Convert responses to lowercase
        occasion = str(responses[1]).lower()
        size = str(responses[2][0]).lower() if isinstance(responses[2], list) and len(responses[2]) > 0 else ''
        BodyType = str(responses[3][0]).lower() if isinstance(responses[3], list) and len(responses[3]) > 0 else ''
        preference = str(responses[4][0]).lower() if isinstance(responses[4], list) and len(responses[4]) > 0 else ''
        price = str(responses[5][0]).lower() if isinstance(responses[5], list) and len(responses[5]) > 0 else ''

        # Read the dataset
        df = pd.read_excel(r'F:/MyntraGPT/Chatbot/Myntras final dataset.xlsx')

        # Adding columns for sizes
        df['is_S'] = df['size'].apply(lambda x: 'S' in x.split(','))
        df['is_M'] = df['size'].apply(lambda x: 'M' in x.split(','))
        df['is_L'] = df['size'].apply(lambda x: 'L' in x.split(','))

        # Adding columns for body types
        df['is_apple'] = df['BodyType'].apply(lambda x: 'apple' in x.split(','))
        df['is_pear'] = df['BodyType'].apply(lambda x: 'pear' in x.split(','))
        df['is_hourglass'] = df['BodyType'].apply(lambda x: 'hourglass' in x.split(','))
        df['is_rectangle'] = df['BodyType'].apply(lambda x: 'rectangle' in x.split(','))

        # Apply the filtering based on the user-defined criteria
        filtered_df = df

        # Filtering logic
        if occasion == 'traditional':
            if size == 'S':
                filtered_df = df[df['is_S']]
                if BodyType == 'apple':
                    filtered_df = filtered_df[filtered_df['is_apple']]
                    if preference == 'light':
                        filtered_df = filtered_df[filtered_df['preference'] == 'light']
                        if price == 'below_2300':
                            filtered_df = filtered_df[filtered_df['price'] < 2300]
                        elif price == 'below_900':
                            filtered_df = filtered_df[filtered_df['price'] < 900]
                        elif price == 'below_1500':
                            filtered_df = filtered_df[filtered_df['price'] < 1500]
                        elif price == 'below_5000':
                            filtered_df = filtered_df[filtered_df['price'] < 5000]
                    elif preference == 'dark':
                        filtered_df = filtered_df[filtered_df['preference'] == 'dark']
                        if price == 'below_2300':
                            filtered_df = filtered_df[filtered_df['price'] < 2300]
                        elif price == 'below_900':
                            filtered_df = filtered_df[filtered_df['price'] < 900]
                        elif price == 'below_1500':
                            filtered_df = filtered_df[filtered_df['price'] < 1500]
                        elif price == 'below_5000':
                            filtered_df = filtered_df[filtered_df['price'] < 5000]
            elif size == 'M':
                filtered_df = df[df['is_M']]
                if BodyType == 'apple':
                    filtered_df = filtered_df[filtered_df['is_apple']]
                    if preference == 'light':
                        filtered_df = filtered_df[filtered_df['preference'] == 'light']
                        if price == 'below_2300':
                            filtered_df = filtered_df[filtered_df['price'] < 2300]
                        elif price == 'below_900':
                            filtered_df = filtered_df[filtered_df['price'] < 900]
                        elif price == 'below_1500':
                            filtered_df = filtered_df[filtered_df['price'] < 1500]
                        elif price == 'below_5000':
                            filtered_df = filtered_df[filtered_df['price'] < 5000]
                    elif preference == 'dark':
                        filtered_df = filtered_df[filtered_df['preference'] == 'dark']
                        if price == 'below_2300':
                            filtered_df = filtered_df[filtered_df['price'] < 2300]
                        elif price == 'below_900':
                            filtered_df = filtered_df[filtered_df['price'] < 900]
                        elif price == 'below_1500':
                            filtered_df = filtered_df[filtered_df['price'] < 1500]
                        elif price == 'below_5000':
                            filtered_df = filtered_df[filtered_df['price'] < 5000]
            elif size == 'L':
                filtered_df = df[df['is_L']]
                if BodyType == 'apple':
                    filtered_df = filtered_df[filtered_df['is_apple']]
                    if preference == 'light':
                        filtered_df = filtered_df[filtered_df['preference'] == 'light']
                        if price == 'below_2300':
                            filtered_df = filtered_df[filtered_df['price'] < 2300]
                        elif price == 'below_900':
                            filtered_df = filtered_df[filtered_df['price'] < 900]
                        elif price == 'below_1500':
                            filtered_df = filtered_df[filtered_df['price'] < 1500]
                        elif price == 'below_5000':
                            filtered_df = filtered_df[filtered_df['price'] < 5000]
                    elif preference == 'dark':
                        filtered_df = filtered_df[filtered_df['preference'] == 'dark']
                        if price == 'below_2300':
                            filtered_df = filtered_df[filtered_df['price'] < 2300]
                        elif price == 'below_900':
                            filtered_df = filtered_df[filtered_df['price'] < 900]
                        elif price == 'below_1500':
                            filtered_df = filtered_df[filtered_df['price'] < 1500]
                        elif price == 'below_5000':
                            filtered_df = filtered_df[filtered_df['price'] < 5000]
        elif occasion == 'western':
            if size == 'S':
                filtered_df = df[df['is_S']]
                if BodyType == 'apple':
                    filtered_df = filtered_df[filtered_df['is_apple']]
                    if preference == 'light':
                        filtered_df = filtered_df[filtered_df['preference'] == 'light']
                        if price == 'below_2300':
                            filtered_df = filtered_df[filtered_df['price'] < 2300]
                        elif price == 'below_900':
                            filtered_df = filtered_df[filtered_df['price'] < 900]
                        elif price == 'below_1500':
                            filtered_df = filtered_df[filtered_df['price'] < 1500]
                        elif price == 'below_5000':
                            filtered_df = filtered_df[filtered_df['price'] < 5000]
                    elif preference == 'dark':
                        filtered_df = filtered_df[filtered_df['preference'] == 'dark']
                        if price == 'below_2300':
                            filtered_df = filtered_df[filtered_df['price'] < 2300]
                        elif price == 'below_900':
                            filtered_df = filtered_df[filtered_df['price'] < 900]
                        elif price == 'below_1500':
                            filtered_df = filtered_df[filtered_df['price'] < 1500]
                        elif price == 'below_5000':
                            filtered_df = filtered_df[filtered_df['price'] < 5000]
            elif size == 'M':
                filtered_df = df[df['is_M']]
                if BodyType == 'apple':
                    filtered_df = filtered_df[filtered_df['is_apple']]
                    if preference == 'light':
                        filtered_df = filtered_df[filtered_df['preference'] == 'light']
                        if price == 'below_2300':
                            filtered_df = filtered_df[filtered_df['price'] < 2300]
                        elif price == 'below_900':
                            filtered_df = filtered_df[filtered_df['price'] < 900]
                        elif price == 'below_1500':
                            filtered_df = filtered_df[filtered_df['price'] < 1500]
                        elif price == 'below_5000':
                            filtered_df = filtered_df[filtered_df['price'] < 5000]
                    elif preference == 'dark':
                        filtered_df = filtered_df[filtered_df['preference'] == 'dark']
                        if price == 'below_2300':
                            filtered_df = filtered_df[filtered_df['price'] < 2300]
                        elif price == 'below_900':
                            filtered_df = filtered_df[filtered_df['price'] < 900]
                        elif price == 'below_1500':
                            filtered_df = filtered_df[filtered_df['price'] < 1500]
                        elif price == 'below_5000':
                            filtered_df = filtered_df[filtered_df['price'] < 5000]
        else:
            return jsonify({'error': 'Invalid occasion'}), 400

        # Return recommendations
        recommendations = filtered_df.to_dict(orient='records')
        return jsonify(recommendations)
    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
