import React from 'react'
import ReactDOM from 'react-dom'
import Axios from 'axios';

class Login extends React.Component{

    constructor(props){
        super(props);
        this.state = {}
    }


    async UNSAFE_componentWillMount(){
        this.setState({
            schema : [],
            urls: {},
            data: {}
        })
    }

    async componentDidMount(){
        Axios.get('/api/login/user/schema').then(res => {
            console.log(res.data)
            let data = {}
            res.data.schema.forEach(fields => {
                data[fields.name] = ""
            })
            this.setState({
                schema : res.data.schema,
                urls: res.data.urls,
                data: data
            })
        })
    }

    handleChange(event){
        let data = this.state.data
        let { name, value } = event.target;
        data[name] = value;
        this.setState({
            data:data
        })
    }

    handleSubmit(){
        let urls = this.state.urls
        let data = this.state.data
        Axios.post(urls['submit_url'], data).then(res => {
            console.log(res.data.status)
        })
    }

    render(){
        let input = []
        this.state.schema.forEach(tag => {
            input.push(
                <div>
                    <label>{tag['field_name']}</label>
                    <input type={tag["type"]} name={tag['name']} onChange={(e)=>this.handleChange(e)} required/>
                </div>
            )
        })

        return(
            <form>
                {input}
                <button onClick={()=>this.handleSubmit()}>Log In</button>
            </form>
        )
    }
}

ReactDOM.render(<Login/>, document.getElementById('login-main-container'));


