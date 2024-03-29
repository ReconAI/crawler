// jsx code
'use strict';

class ResultItem extends React.Component {
    constructor(props) {
        super(props);
        this.handlePlayClick = this.handlePlayClick.bind(this);
        this.handlePauseClick = this.handlePauseClick.bind(this);
        this.handleConfirmClick = this.handleConfirmClick.bind(this);
        this.handleDiscardClick = this.handleDiscardClick.bind(this);
        this.handleVideoLinkClick = this.handleVideoLinkClick.bind(this);
        this.state = {'isHidden': false};
    }
    handleVideoLinkClick(event) {
        event.preventDefault();
        // todo: think about React approach for this place
        $('#quickview .modal-body').html('<div class="embed-responsive embed-responsive-16by9"><iframe class="embed-responsive-item" id="embed-video" src="' + this.props.item.embedded_link + '" allowfullscreen></iframe></div>');
        $('#quickview').modal({show:true});
    }

    handlePlayClick() {
        let video_id = document.getElementById("video_"+this.props.item.id);
        video_id.play();
    }

    handlePauseClick() {
        let video_id = document.getElementById("video_"+this.props.item.id);
        video_id.pause();
    }
    handleConfirmClick() {
        $.ajax({
            method: "PUT",
            url: serverHost + "api/search-results/"+this.props.item.id+ "/status/",
            data: {"status": 'CONFIRMED'}
        }).done(function (data) {
            console.log(data);
            alert('Video is confirmed')
        });
    }

    handleDiscardClick() {
        $.ajax({
            method: "PUT",
            url: serverHost + "api/search-results/"+this.props.item.id+ "/status/",
            data: {"status": 'DISCARDED'}
        }).done(function (data) {
            console.log(data);
            alert('Video is discarded')
        });
        this.setState({'isHidden': true});
    }

  render () {
    let poster;
    if (this.props.item.preview_link == undefined){
        poster = 'static/img/processing.png';
    }
    else {
        poster='';
    }
    if (this.state.isHidden) {
        return null
    }

    return (
        <div className='row border col-sm-12 col-md-12 col-lg-12 resultItem'>
                <div className='col-sm-6'>
                    <div className='row'>
                        <div className='col-sm-10'>
                            <p className='h5'><a href={this.props.item.source_link} onClick={this.handleVideoLinkClick}>{this.props.item.source_link}</a></p>
                            <div className='embed-responsive embed-responsive-16by9'>
                                <video id={"video_"+this.props.item.id} poster={poster}>
                                 <source src={this.props.item.preview_link} type="video/ogg"/>
                                </video>
                            </div>
                        </div>
                        <div
                            className='col-sm-2 col-md-2 col-lg-2 d-flex flex-column justify-content-center align-items-start'>
                            <button type='button' className='btn btn-outline-secondary player-button'><img src='static/img/player.svg' onClick={this.handlePauseClick}/></button>
                            <button type='button' className='btn btn-outline-secondary'><img src='static/img/interface.svg' onClick={this.handlePlayClick}/></button>
                        </div>
                    </div>
                </div>
                <div className='col-sm-6 col-md-6 col-lg-6'>
                    <p className='h5'>Video details:</p>
                    <div className='container border video-details-wrapper1'>
                        <div className='video-details-wrapper2'>
                            <div className='video-details-wrapper3'>
                                <label className='form-check-label' htmlFor='defaultCheck1'>
                                    Video title:
                                </label>
                                <label className='form-check-label' htmlFor='defaultCheck1'>
                                    Published at:
                                </label>
                                <label className='form-check-label' htmlFor='defaultCheck1'>
                                    Duration:
                                </label>
                                <label className='form-check-label' htmlFor='defaultCheck1'>
                                    Width:
                                </label>
                                <label className='form-check-label' htmlFor='defaultCheck1'>
                                    Height:
                                </label>
                            </div>
                            <div className='video-details-wrapper-values'>
                                <label className='form-check-label' htmlFor='defaultCheck1'>
                                    {this.props.item.video_title}
                                </label>
                                <label className='form-check-label' htmlFor='defaultCheck1'>
                                    {this.props.item.published_at}
                                </label>
                                <label className='form-check-label' htmlFor='defaultCheck1'>
                                    {this.props.item.duration}
                                </label>
                                <label className='form-check-label' htmlFor='defaultCheck1'>
                                    {this.props.item.width}
                                </label>
                                <label className='form-check-label' htmlFor='defaultCheck1'>
                                    {this.props.item.height}
                                </label>
                            </div>
                        </div>
                    </div>
                    <div className='container video-details-button-wrapper'>
                        <button type='button' className='btn btn-secondary confirm-discard-button' onClick={this.handleConfirmClick}>Confirm</button>
                        <button type='button' className='btn btn-secondary confirm-discard-button' onClick={this.handleDiscardClick}>Discard</button>
                    </div>
                </div>
            </div>

    );
  }
}

class PrevNext extends React.Component {
    constructor(props) {
        super(props);
        this.handleNextClick = this.handleNextClick.bind(this);
        this.handlePreviousClick = this.handlePreviousClick.bind(this);
    }
    handleNextClick(event) {
        event.preventDefault();
        api_read_results(null, this.props.next)

    }
    handlePreviousClick(event) {
        event.preventDefault();
        api_read_results(null, this.props.previous)
    }

    render() {
        let href_next='';
        let disabled_next = '';
        let disabled_previous = '';
        if (this.props.next) {
            href_next="#"
        }
        else {
            disabled_next='disabled'
        }
        let href_previous='';
        if (this.props.previous) {
            href_previous="#"
        }
        else {
            disabled_previous='disabled'
        }
        return (
            <div>
                <a href="#" onClick={this.handlePreviousClick} className={"btn " + disabled_previous}>Previous</a> &nbsp;
                <a href="#" onClick={this.handleNextClick} className={"btn " + disabled_next}>Next</a>
            </div>
        );
    }
}

class SearchResult extends React.Component {
  render() {
    return (
        <div>
          {this.props.data['results'].map(item => {
            return <ResultItem item={item} key={item.source_link}/>
          })}
          <PrevNext next={this.props.data.next} previous={this.props.data.previous}/>
        </div>
    );
  }
}






