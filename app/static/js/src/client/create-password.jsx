import React from 'react'
import ReactDOM from 'react-dom'
import Axios from 'axios';
import { Redirect } from '../components/Redirect.jsx';


class CreatePassword extends React.Component {
    constructor(props){
        super(props);
        this.state = {}
    }
    
    async UNSAFE_componentWillMount(){
        let data = {"password": "", "confirm_password": ""}
        this.setState({
            data: data,
            error_message: "",
            password_created: false
        })
    }



    async componentDidMount(){
        let data = {"password": "", "confirm_password": "", "email": this.props.email}
        this.setState({
            data: data,
            error_message: "",
            password_created: false
        })
    }

    handleChange(event){
        const { name, value } = event.target

        let data = this.state.data
        data[name] = value
        this.setState({data:data})
    }

    handleSubmit(){
        let url = '/api/password/create'
        let data = this.state.data
        if(data["password"] === data["confirm_password"]){
            Axios.post(url, data).then(res => {
                res.data.status ? this.setState({password_created:true}) : this.setState({error_message: res.data.message})
            })
        }
        else{
            this.setState({
                error_message: "Password not matched"
            })
        }
        
    }

    render() {

        let redirect_message=[]

        redirect_message.push(
            <div>
                Password created Succesfully
                <div>You will be redirected to login page.<a href="/login">Click Here</a></div>
            </div>
        )


        return (
           <div>
               {this.state.error_message ? <div>{this.state.error_message}</div>:""}
               { this.state.password_created ? <Redirect timeout={5000} redirect_url={'/login'} message={redirect_message}/>:
                    <div>
                        <label>New password</label>
                        <input type="password" name="password" value={this.state.data.password} onChange={(e)=>this.handleChange(e)}></input>
                        <label>Confirm password</label>
                        <input type="password" name="confirm_password" value={this.state.data.confirm_password} onChange={(e)=>this.handleChange(e)}></input>
                        <button onClick={()=>this.handleSubmit()}>Create password</button>
                    </div>
               }
           </div>
        );
    }
  }

  ReactDOM.render(<CreatePassword email={email}/>, document.getElementById('create-password-main-container'));
